#
# S7 FPGA PA verify program
#
# To generate test data or weight data
# read test case file and input test pattern to generate test data file
#
#   $python3 gendata.py data.json
# 
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import json
from utility import * 



def main():
	#
	# try to open register JSON file
	#
	try:
		file = sys.argv[1]
	except:
		file = input("file name of data:")
	#
	# input test data pattern and weight pattern
	#
	data = query_value("data pattern(0~255): ", 0, 255)
	total = query_value("data size(1~4608): ", 1, 48 * 96)
	weight = query_yes_no("generate weight data:","no")
	size = 0

	try:
		fd = open(file, "wb")
	except:
		print("open file " + file + "fail")
		return

	while total > 0:
		if weight==True:
			#fd.write(data.to_bytes(4, 'big'))
			fd.write(data.to_bytes(4, 'little'))
			total -=4
			size += 4
		else:
			fd.write(data.to_bytes(1, 'little')) 
			total -=1

	if weight==True:
		pad=0
		while size < 96:
			#fd.write(pad.to_bytes(4, 'big')) 
			fd.write(pad.to_bytes(4, 'little')) 
			size+=4
	fd.close()

	return


# start program
if __name__ == '__main__':
	main()