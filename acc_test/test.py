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
# start main program
#
def main():
	parser = argparse.ArgumentParser(description="The program will do peripheral functions test.")
	parser.add_argument("file",help="input JSON format registers data file")
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
	return
	
#
# end main progam
#
if __name__ == '__main__':
	main()
	
'''
from __future__ import print_function
import numpy as np



E = np.array([
	[0,0,0],
	[1,0,0],
	[0,1,0],
	[0,0,1],
	[0,0,0]
])

print(E.size)
num_rows = np.shape(E)[0]
num_cols = np.shape(E)[1]
print("rows="+str(num_rows)+", clos="+str(num_cols))

l = E.reshape(E.size)
for i in range(3):
	print(l[num_cols*i:])
	

A=[]
num_rows = np.shape(E)[0]
num_cols = np.shape(E)[1]
print(num_rows)


for i in range(num_rows):
	for j in range(num_cols):
		A.append(E[i,j])
print(A)
'''
'''
C = np.array([
	[1,0,0],
	[0,1,0],
	[0,0,1]
	])

D = np.array([
	[0,0,0,0,0],
	[0,1,0,0,0],
	[0,0,1,0,0],
	[0,0,0,1,0],
	[0,0,0,0,0]
])



for i in range(0,3):
	for j in range(0,3):
		v = D[i:i+3,j:j+3]*C
		print(str(v.sum())+",",end="")
	print("")
'''
