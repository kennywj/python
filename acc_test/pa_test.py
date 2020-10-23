#
# test functions
#
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
from os import path
import re
import json
import time
import math
from utility import *
import subprocess
import argparse

#
# bitfile before 1013
#
#ifm_base = 0x20100000
#ofm_base = 0x20130000
#
# bitfile after 1013
#
ifm_base = 0x44107200
ofm_base = 0x44107300

data_path = "data"

#
# write_IFM
#
def write_IFM(addr, bufsize, f):
	i = 0
	total = 0
	debug_en(False)
	while True:
		data = f.read(4)
		if not data:	# EOF?
			break
		value = int.from_bytes(data, "little")
		writereg(addr,value)
		i += 4
		total += 4
		if i >= bufsize:
			#print("write "+ str(i)+" bytes data to addr " + str(hex(addr)),end='\r')
			print("write "+ str(i)+" bytes data to addr " + str(hex(addr))+" total= " + str(total))
			addr += 4
			i = 0
	if i:
		print("write "+ str(i)+" bytes data to addr " + str(hex(addr))+" total= " + str(total))
	debug_en(True)
	return

#
# all IFM fill one pattern
#
def fill_IFM(base, data):
	val = (data << 24)|(data<<16)|(data<<8)|data
	print("fill IFM with data pattern= "+ str(hex(val)))
	addr = base
	debug_en(False)
	for i in range(48):
		count = 0
		while count < 1024:
			writereg(addr,val)
			count += 4
		print("write "+ str(count * 4)+" bytes "+ str(hex(data)) +" to addr " + str(hex(addr)),end='\r')
		addr += 4
		i += 4
	debug_en(True)
	return

#
# write_weight
#
def write_weight(base, bufsize, f):
	addr = 0
	count = 0
	num = 0
	debug_en(False)
	while True:
		data = f.read(4)
		if not data:	# EOF?
			if addr:
				print("Write ("+str(num)+") weight data " + str(count) + " bytes")
			break
		value = int.from_bytes(data, "little")
		writereg(base+addr,value)
		addr += 4
		count += 4
		if addr >= bufsize:
			#print("Write ("+str(num) +") weight data " + str(count) + " bytes",end='\r')
			print("Write ("+str(num) +") weight data " + str(count) + " bytes")
			addr = 0
			num += 1
	debug_en(True)
	if addr != 0:
		print("touch " + str(hex(base+0x5c)) + " to enable shift")
		writereg(base+0x5c,0)
	return
	
#
# write_bias
#
def write_bias(base, f):
	addr = 0
	while addr < 96:
		data = f.read(4)
		if not data:	# EOF?
			break
		value = int.from_bytes(data, "big")
		writereg(base+addr,value)
		addr += 4
	return	
#
#fill weight 96 * 48 with one pattern
#
def fill_weight(addr, data):
	val = (data << 24)|(data<<16)|(data<<8)|data
	print("fill weight registers with data pattern= "+ str(hex(val)))
	debug_en(False)
	for i in range(48):
		count = 0
		while count < 96:
			writereg(addr,val)
			count += 4
		print("write "+ str(count * 4)+" bytes "+str(hex(data))+" to addr " + str(hex(addr)),end='\r')
		addr += 4
		i += 4
	debug_en(True)
	return

#
# read_OFM
#
def read_OFM(base, n, bufsize, f):
	addr = 0
	total = 0
	mask=[0x000000ff, 0x0000ffff, 0x00ffffff]

	debug_en(False)
	while n>0:
		i=0
		#print("Read "+str(hex(base+addr))+", size= "+str(bufsize),end='\r')
		while i<bufsize:
			value = readreg(base+addr)
			if n < 4:
				value = value & mask[n-1]
				bytes = value.to_bytes(n, 'little')
				total += n
			else:
				bytes = value.to_bytes(4, 'little')
				total += 4
			f.write(bytes)
			i+=1
		print("Read "+str(hex(base+addr))+", size= "+str(bufsize)+" total=" + str(total))
		addr+=4
		n-=4
	debug_en(True)
	print("")
	return


def dump_OFM(base):
	addr = 0
	debug_en(False)
	for i in range(96):
		count = 0
		value=[]
		while count < 1024:
			value.append(readreg(base+addr))
			count +=1
		addr += 4
		i += 4
		print(' '.join(map(str, value)))
	debug_en(True)

#
# get value by key
#
def get_value(db, key):
	if key in db:
		return db[key]
	return 0
#
# parsing the JSON format test case and program PA
#
def do_test(pa, pa_base, cluster, cluster_base, item):
	print(item["comments"])
	#
	# check if PA ready?
	#
	addr = get_addr(cluster, cluster_base, "pa_ststus")
	while True:
		print("Read PA status...")
		val = readreg(addr)
		if (val & 0x01):	# PA ready?
			break
		print("not ready")
		time.sleep(1)
	print("ready to run")
	#
	# retrive parameters
	#

	kernel =  find_index(item["kernel"],["3x3","TBD","1x1","TBD"])
	kernel_num = item["kernel_num"]
	channel_num = item["channel_num"]
	high = item["feature_map_high"]
	width = item["feature_map_width"]
	stride = item["stride"]
	left_right_pad_num = item["left_right_pad_num"]
	top_bottom_pad_num = item["top_bottom_pad_num"]
	dilation = item["dilation"]
	operation = find_index(item["operation"],["convlution","max_pool","average_pool","matrix_addition"])
	de_quantized = item["de-quantized"]
	batch_normal = item["batch_normalization"]
	relu = item["relu"]
	relu6 = item["relu6"]
	yacc_output = item["yacc_output"]
	relu_output = item["relu_output"]
	left_1_pa = item["left_1_pa"]
	yacc_source = item["yacc_source"]
	cluster_cascate = find_index(item["cluster_cascate"],["independent","kernal_cascate","channel_cascate"])
	data_file = item["data"]
	weight_file = item["weight"]
	result_file = item["result"]
	output_file = item["output"]
	enable_pa = 1
	#
	# check DMA enable flag
	#
	if "dma" in item:
		dma_en = item["dma"]
	else:
		dma_en = False
	
	if dma_en == True:
		#
		# load cluster register file
		#
		with open('dma330.json', 'r', encoding='utf-8') as f:
			dma330 = json.load(f)
	
	col = get_num(kernel, kernel_num)
	row = get_num(kernel, channel_num)
	
	#
	# program cluster configuration
	#
	print("Program cluster configuration")
	# cascate mode
	writereg(get_addr(cluster, cluster_base, "cluster_control"),cluster_cascate | (dma_en<<3))
	# clear ofm counter
	print("Clear OFM counter")
	writereg(get_addr(cluster, cluster_base, "ofm_clear_counter"),0x01)
	# write input feature map y, x
	print("Write Cluster pa0 input feature map")
	writereg(get_addr(cluster, cluster_base, "pa0_input_feature_map"),(width<<16 | high))
	
	#
	# write data to Input Frame Memory
	#
	# clear ifm counter
	rel_path = data_path + "/" + data_file
	writereg(get_addr(cluster, cluster_base, "ifm_clear_counter"),0x01)
	try:
		with open(rel_path, 'rb') as f:
			print("fill IFM by file "+ rel_path + ", size=" + str(os.stat(rel_path).st_size))
			write_IFM(ifm_base, os.stat(rel_path).st_size/math.ceil(row/4) , f)
	except:
		# convert sting to int value
		data = int(data_file, 16)
		fill_IFM(ifm_base, data)
	counter = readreg(get_addr(cluster, cluster_base, "ifm_counter"))
	print("IFM counter = "+ str(counter))
	#
	# write weight to weight register
	#
	rel_path = data_path + "/" + weight_file
	try:
		with open(rel_path, 'rb') as f:
			print("fill weight buffer by file "+ rel_path + ", size=" + str(os.stat(rel_path).st_size))
			write_weight(get_addr(cluster, cluster_base, "pa0_in_weight_3_0"), 96, f)
	except:
		# convert sting to int value
		data = int(weight_file, 16)
		fill_weight(get_addr(cluster, cluster_base, "pa0_in_weight_3_0"), data)
	
	#
	# program cascate and DMA configuration
	#
	print("Program PA configuration")
	# pe_config1
	pe_config1 = (kernel&0x03)<<30 | (int(relu6))<<29 |((stride-1)&0x03)<<27 | (left_right_pad_num & 0x7)<<24	\
		| (row<<8) | col
	writereg(get_addr(pa, pa_base, "pe_config1"),pe_config1)

	# pe_config2
	if kernel == 0: # kernel 3x3
		pe_config2 = width<<24|high<<16|((width+left_right_pad_num*2)-2)<<8|(high+left_right_pad_num*2)-2
	else:
		pe_config2 = width<<24|high<<16|(width+left_right_pad_num*2)<<8|(high+left_right_pad_num*2)
	writereg(get_addr(pa, pa_base, "pe_config2") ,pe_config2)

	# row pass and column pass
	row_pass=[0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
	row_pass = bitmask(row, row_pass)
	writereg(get_addr(pa, pa_base, "row_pass1"),row_pass[0])
	writereg(get_addr(pa, pa_base, "row_pass2"),row_pass[1])
	writereg(get_addr(pa, pa_base, "row_pass3"),row_pass[2])

	col_pass=[0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
	col_pass = bitmask(col, col_pass)
	writereg(get_addr(pa, pa_base, "col_pass1"),col_pass[0])
	writereg(get_addr(pa, pa_base, "col_pass2"),col_pass[1])
	writereg(get_addr(pa, pa_base, "col_pass3"),col_pass[2])

	# control
	#Bit[21] : dq_bypass
    #          "H"  Disable   "De-quantized Block"  ==> high: disable bypass => do De-quantized => true
    #          "L"  Enable   "De-quantized Block"   ==> low: enable bypass => not do De-quantized => false
	#Bit[20] :  bn_bypass
    #          "H"  Disable   "Batch-normalization Block"
    #          "L"  Enable   "Batch-normalization Block"
	#Bit[19] :  relu_bypass
    #          "H"  Disable   "RELU Block"
    #          "L"  Enable   "RELU Block"
	# low enable: de_quantized, batch_normal, relu
	#
	control = (int(not de_quantized)<<21) | (int(not batch_normal)<<20) | (int(not relu)<<19)  \
		| ((operation&0x07)<<16) | (int(not yacc_output)<<7) | (int(not relu_output)<<6) \
		| (left_1_pa<<5) | ((yacc_source&0x3)<<3)
	writereg(get_addr(pa, pa_base, "control"),control)

	# De_qantized_mult
	if "De_qantized_mult" in item:
		print("Write de-quantied multiply coffecient")
		writereg(get_addr(pa, pa_base, "De_qantized_mult"),int(item["De_qantized_mult"],16))
	if "De_quantized_bias" in item:
		addr = get_addr(pa, pa_base, "De_quantized_bias3_0")
		if type(item["De_quantized_bias"])==str:
			rel_bias_path = data_path + "/" + item["De_quantized_bias"]
			with open(rel_bias_path, 'rb') as f:
				print("Write de-quantized bias by file "+ rel_bias_path + ", size=" + str(os.stat(rel_bias_path).st_size))
				write_bias(addr, f)
		else:
			print("Write de-quantied bias by array")
			for i in item["De_quantized_bias"]:
				writereg(addr,int(i,16))
				addr += 4
	#
	# enable PA operation
	#
	print("Enable PA0")
	control = (dilation&0x07)<<5 | ((top_bottom_pad_num&0x07)<<2) | enable_pa
	writereg(get_addr(cluster, cluster_base, "pa_control"),control)
	# check status
	addr = get_addr(cluster, cluster_base, "pa_ststus")
	while True:
		print("Read PA status...")
		status = readreg(addr)
		if (status & 0x01):	# PA ready?
			break
		print("is working")
		time.sleep(1)
	print("done")
	print("PA status= " + str(hex(status)))
	counter = readreg(get_addr(cluster, cluster_base, "pa0_counter"))
	print("PA counter= " + str(hex(counter)) + " ("+ str(counter) +")")
	counter = readreg(get_addr(cluster, cluster_base, "ofm_counter"))
	print("OFM counter = "+ str(counter))
	# read OFM and write to temp file
	# high and width 要考慮padding 真正size 是??
	rel_output_path = data_path + "/" + output_file
	try:
		with open(rel_output_path, 'wb') as f:
			if kernel == 0: # kernel 3x3
				high = (high+left_right_pad_num*2)-2
				width = (width+left_right_pad_num*2)-2
			print("read OFM buffer, kernel num= "+ str(kernel_num) + ", size= " + str(high * width) + ", write to file " + rel_output_path)
			read_OFM(ofm_base, kernel_num, high * width, f)
	except IOError:
		# dump OFM contain
		dump_OFM(ofm_base)

	#
	# compare temp file and result file, if equal, show "success", else show "fail"
	#
	rel_result_path = data_path + "/" + result_file
	if path.exists(rel_result_path):
		
		out = subprocess.Popen(['cmp', '-l', rel_output_path, rel_result_path],
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
		stdout,stderr = out.communicate()
		msg = stdout.decode("utf-8").split('\n')
		if len(msg)>1:
			for i in range(0,len(msg)-1):
				if re.search("EOF",msg[i]):
					print("    reach EOF")
					break
				l = msg[i].strip(' \t\n').split()
				print("   " + str(l[0]) + " " + str(hex(int(l[1],8))) + " " + str(hex(int(l[2],8))))
				if i>10:
					print("    Too many errors, ignore other errors!")
					break
		print("*** compare " + rel_output_path  + " , " + rel_result_path+" error= " + str(len(msg)-1))
	else:
		print("without file " + rel_result_path + ", not do compare")
	return
#
# start of test program
# usage: python3 pa_test.py [<file of test case> <HOST> <test case index>]
#
def main():

	parser = argparse.ArgumentParser(description="The program applied to verify the PA's features")
	parser.add_argument("file",help="input JSON format test cases file")
	parser.add_argument("host",help="input traget's IP address")
	parser.add_argument("-t","--test", dest="test", help="specified test case to do test")
	parser.add_argument("-o","--output", dest="log", help="output test result to file")
	args = parser.parse_args()
	
	# do connect HOST
	if not connect(args.host):
		return

	#
	# load pa egister file
	#
	with open('pa_regs.json', 'r', encoding='utf-8') as f:
		pa_regs = json.load(f)
		
	pa = pa_regs["pa"]["regs"]
	pa_base = int(pa_regs["pa"]["base"],16)
	cluster = pa_regs["cluster"]["regs"]
	cluster_base = int(pa_regs["cluster"]["base"],16)
	
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
	# reset PA/cluster
	#
	do_reset(cluster, cluster_base)

	#
	# open test case JSON file
	#
	with open(args.file, 'r', encoding='utf-8') as f:
		output = json.load(f)

	if args.test:
		# select test index to do test
		if args.test in output:
			print("*** [start] Do test "+ args.test + " ***")
			do_test(pa, pa_base, cluster, cluster_base, output[args.test])
			print("*** [end] ***")
		else:
			print("Test case " + args.test + " not exist!")
	else:
		keys = output.keys()
		for i in keys:
			print("*** [start] Do test "+ i + " ***")
			do_test(pa, pa_base, cluster, cluster_base, output[i])
			print("*** [end] ***")
	
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
