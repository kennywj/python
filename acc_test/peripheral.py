#
# test PA's registers module
#
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import re
import time
from utility import *
from collections import OrderedDict
import argparse

#
# parsing the JSON format test case and program PA
# mask : reserver bits, write only bits, enable operation bits or reset bits, not test
#
def do_regs_test(reg, base, item):

	enable = item["enable"]
	offset = int(item["offset"],16)
	mask = int(item["mask"],16)
	default = int(item["default"],16)
	type = item["type"]

	addr = base+offset
	print("\"" + reg + "\": addr="+ str(hex(addr)) + ", default=" + str(hex(default))+", mask= "+str(hex(mask)))

	# check whether register needs to do test
	if enable==False:
		print("   Ignore test\n")
		return 0
		
	# do write test for write only register
	if type=="wo":
		val_0 = 0xFFFFFFFF ^ mask
		writereg(addr, val_0)
		print("   Write " + str(hex(val_0)) + " to " + str(hex(addr)))
		print("   Write only register, not to do read test.\n")
		return 0

	# read register and then and with invert mask should same as default
	val = readreg(addr)
	print("   Read " + str(hex(addr))+ ", value=" + str(hex(val)), end='')
	if val != default:
		print(" [fail]\n   Not do other test.\n")
		return 1
	else:
		print(" [success]")

	if type=="ro":
		print("   Read only register, not to do write test.\n")
		return 0

	# write mask to register and read back should same as mask
	count = 0
	val_0 = (0xFFFFFFFF ^ mask)
	writereg(addr, val_0)
	val_1 = (readreg(addr) & ~mask)
	print("   1. Write " + str(hex(val_0)) + " to " + str(hex(addr))+ ", then read value="+ str(hex(val_1)), end='')
	if val_0 == val_1:
		print(" [success]")
	else:
		print(" [fail]")
		count += 1

	# write 0 to register and read back should same as mask
	val_0 = 0x00000000 ^ mask
	writereg(addr, val_0)
	val_1 = readreg(addr) & ~mask
	print("   2. Write "+ str(hex(val_0))+" to " + str(hex(addr)) + ", then read value="+ str(hex(val_1)), end='')
	if val_1 == 0:
		print(" [success]")
	else:
		print(" [fail]")
		count += 1

	writereg(addr, default & mask)
	print("\n")
	return count

#
# select specified IP to do test
#

def do_ip_test(peripheral, ip):
	error = 0
	if peripheral[ip]['enable']==True:
		print("Enable to do test " + ip)
		base = int(peripheral[ip]['base'],16)
		regs = peripheral[ip]['regs']
		keys = regs.keys()
		debug_en(False)
		for i in keys:
			error += do_regs_test(i, base, regs[i])
		debug_en(True)
	else:
		print("Not enable to do test " + ip)
	return error
#
# main routine to do register test
#
def main():
	curr = ""
	parser = argparse.ArgumentParser(description="The program will read/write verification of the device's registers.")
	parser.add_argument("file",help="input JSON format registers data file")
	parser.add_argument("host",help="input traget's IP address")
	parser.add_argument("-o","--output", dest="log", help="output test result to file")
	parser.add_argument("-d","--device", dest="ip", help="input specificed IP to do test")
	args = parser.parse_args()
	
	if args.log:
		try:
			f = open(args.log, 'w')
			original_stdout = sys.stdout
			print("Write test result to file " + args.log)
			sys.stdout = f # Change the standard output to the file we created.
		except IOError:
			print("Open file " + args.log + " fail")
			return
			
	#
	# connect to target
	#
	if not connect(args.host):
		if args.log:
			sys.stdout = original_stdout # Reset the standard output to its original value
			f.close()
		return
	
	with open(args.file, 'r', encoding='utf-8') as f:
		peripheral = json.load(f, object_pairs_hook=OrderedDict)
		
	error= 0
	debug_en(False)
	devices = peripheral.keys()
	if args.ip and args.ip in devices:
		if args.ip == "target":
			if curr != args.ip:
				curr = targets(peripheral[args.ip])
		else:
			print("\n***[start] "+ args.ip +" Registers read/write test ***\n")
			error += do_ip_test(peripheral, args.ip)
			if error:
				print("\n*** [end] Test fail, error=" + str(error) + " ***\n")
			else:
				print("\n*** [end] Test success. ***\n")
	else:
		for d in devices:
			if d == "target":
				if curr != d:
					curr = targets(peripheral[d])
			else:
				print("\n***[start] "+ d +" Registers read/write test ***\n")
				error += do_ip_test(peripheral, d)
				if error:
					print("\n*** [end] Test fail, error=" + str(error) + " ***\n")
				else:
					print("\n*** [end] Test success. ***\n")
				error = 0
	debug_en(True)
	
	if args.log:
		sys.stdout = original_stdout # Reset the standard output to its original value
		f.close()
	#
	# end of seeion
	#
	disconnect()
	
	
	return

# start program
if __name__ == '__main__':
	main()
