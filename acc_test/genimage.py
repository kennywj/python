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
	high = query_value("image high size(1~224): ", 1, 224)
	width = query_value("image width size(1~224): ", 1, 224)
	padding = query_value("padding size(1~7): ", 0, 7)
	size = 0
	zero = 0
	
	try:
		fd = open(file, "wb")
	except:
		print("open file " + file + "fail")
		return
	#
	# generate image (high * width)
	# if padding (high+padding*2)*(width + padding*2)
	# for example if image 5x5 padding 1, data 3 ==> generate 7x7
	#	0 0 0 0 0 0 0
	#	0 3 3 3 3 3 0
	#	0 3 3 3 3 3 0
	#	0 3 3 3 3 3 0
	#	0 3 3 3 3 3 0
	#	0 3 3 3 3 3 0
	#	0 0 0 0 0 0 0
	#
	# fill zero first rows
	for h in range(padding):
		for w in range(width+padding*2):
			fd.write(zero.to_bytes(1, 'little'))
	# fill data row
	for h in range(high):
		# fill leading zeros
		for w in range(padding):
			fd.write(zero.to_bytes(1, 'little'))
		# fill data 
		for w in range(width):
			fd.write(data.to_bytes(1, 'little'))
		# fill ending zeros
		for w in range(padding):
			fd.write(zero.to_bytes(1, 'little'))
	
	# fill zero last rows
	for h in range(padding):
		for w in range(width+padding*2):
			fd.write(zero.to_bytes(1, 'little'))
			
	fd.close()
	
	# display image
	with open(file, 'rb') as f:
		for h in range(high+padding*2):
			for w in range(width+padding*2):
				data = f.read(1)
				if not data:	# EOF?
					break
				print(hex(int.from_bytes(data,'little'))[2:].zfill(2) + " ",end="")
			print("")
			
	print("Generate data for 3x3 kernel")
	cols=[]
	rows=[]
	with open(file, 'rb') as f:
		for h in range(high+padding*2):
			for w in range(width+padding*2):
				data = f.read(1)
				if not data:	# EOF?
					break
				cols.append(int.from_bytes(data,'little'))
			rows.append(row)
	image=[]		
	for i in range(len(rows)):
		print(str(i) + ":",end="")
		print(image[i])
	return


# start program
if __name__ == '__main__':
	main()