#!/usr/bin/python
#
# test.py
#
from __future__ import print_function
import re
import json
import sys
import os
from os import path
from utility import * 
import argparse

#
# do uart test function
#
def do_uart_test(regs, peram):
	print("do_uart_test")
	
	
#
# do timer test function
#
def do_uart_test(regs, peram):
	print("do_timer_test")
	

#
# do watchdog test function
#
def do_watchdog_test(regs, peram):
	print("do_watchdog_test")
	

#
# do hdma test function
#
def do_hdma_test(regs, peram):
	print("do_hdma_test")
	
	
peri_func = {
	"uart"	:	{"func":do_uart_test,"param":[]},
	"timer"	:	{"func":do_timer_test,"param":[]},
	"watchdog":	{"func":do_watchdog_test,"param":[]},
	"hdma"	:	{"func":do_hdma_test,"param":[]}
}

#
# select specified IP to do test
#

def do_ip_test(peripheral, ip):
	error = 0
	if ip in peri_func:
		func = peri_func[ip]["func"]
		func(peripheral[ip], peri_func[ip]["param"])
	else:
		print("The " + ip + " test function not exit")
	return

#
# start main program
#
def main():
	parser = argparse.ArgumentParser(description="The program will do peripheral functions test.")
	parser.add_argument("file",help="input JSON format peripheral registers data file")
	parser.add_argument("host",help="input traget's IP address")
	parser.add_argument("-o","--output", help="output log file")
	parser.add_argument("-d","--device", dest="ip", help="input specificed peripheral to do test")
	
	args = parser.parse_args()
	print("file = " + args.file)
	print("target address = " + args.host)
	if args.output:
		print("output log file " + args.output)
	
	if args.ip:
		print("Do test " + args.ip)
	else:
		print("Do test all devices")
	
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
			print("\n***[start] "+ args.ip +" function test ***\n")
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
				print("\n***[start] "+ d +" function test ***\n")
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
	
#
# end main progam
#
if __name__ == '__main__':
	main()
	
