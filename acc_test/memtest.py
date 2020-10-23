#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import json
from collections import OrderedDict
from utility import *


#
# do memory test
#
def test_mem(name, mem):
	if mem["enable"]==True:
		print("*** [start] Do test "+ name +" : base = "+ mem["base"]+", size = " + mem["size"] +" ***")
		do_memtest(mem["base"],mem["size"])
		print("\n*** [end] ***\n")
	return

#
# start of test program
# usage: python3 pa_test.py [<file of test case> <HOST> <test case index>]
#
def main():
	#
	# try to open register JSON file
	#
	try:
		rel_path = sys.argv[1]
	except:
		rel_path = input("Input file name to do memory test:")
	
	#
	# input HOST IO
	#
	try:
		HOST = sys.argv[2]
	except:
		HOST = input("Enter host IP: ")
	if not connect(HOST):
		return
	
	#
	# select test cpu
	#
	try:
		cpu = sys.argv[3]
	except:
		cpu = None
	# 
	# load cluster register file
	#
	with open(rel_path, 'r', encoding='utf-8') as f:
		module = json.load(f, object_pairs_hook=OrderedDict)
		
	#
	# extend keep_alive timer
	#
	do_set_remotetimeout(3000)
	
	curr = ""
	keys = module.keys()
	if cpu in keys:
		if "target" in module[cpu].keys():
			if curr != module[cpu]["target"]:
				curr = targets(module[cpu]["target"])
		for d in module[cpu]["mem"]:
			test_mem(d, module[cpu]["mem"][d])
	else:	
		for m in keys:
			if "target" in module[m].keys():
				if curr != module[m]["target"]:
					curr = targets(module[m]["target"])
			for d in module[m]["mem"]:
				test_mem(d, module[m]["mem"][d])
	#
	# end of seeion
	#
	disconnect()
	return
	
# start program
if __name__ == '__main__':
	main()