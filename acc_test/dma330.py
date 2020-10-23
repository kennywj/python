#!/usr/bin/python
#
# dma330.py, do DMA 330 test
# Usage: python3 dma330.py <DMA330 program> [output binary data (option)]
#

from __future__ import print_function
import re
import json
import sys
import os
from os import path
from utility import * 
from dmautil import *

# DCCM base address 
insts_base = 0x63200000

#
# dump channel registers
# parameter: channel number, channel register set
#
def dump_regs(n, ch):

	regs = ch["regs"]
	base = int(ch["base"],16)
	
	ftr = readreg(get_addr(regs, base, "FTR"))
	csr = readreg(get_addr(regs, base, "CSR"))
	cpc = readreg(get_addr(regs, base, "CPC"))
	sar = readreg(get_addr(regs, base, "SAR"))
	dar = readreg(get_addr(regs, base, "DAR"))
	ccr = readreg(get_addr(regs, base, "CCR"))
	lc0 = readreg(get_addr(regs, base, "LC0"))
	lc1 = readreg(get_addr(regs, base, "LC1"))
	
	print("\n\t<< CH"+ str(n) +" >>")
	print("\tFTR= 0x"+ str(hex(ftr)[2:].zfill(8)) + ", CSR= 0x" + str(hex(csr)[2:].zfill(8)) + 
		", CPC= 0x" + str(hex(cpc)[2:].zfill(8)) + ", SAR= 0x" + str(hex(sar)[2:].zfill(8)))
	print("\tDAR= 0x"+ str(hex(dar)[2:].zfill(8)) + ", CCR= 0x" + str(hex(ccr)[2:].zfill(8)) + 
		", LC0= 0x" + str(hex(lc0)[2:].zfill(8)) + ", LC1= 0x" + str(hex(lc1)[2:].zfill(8)))
	return

#
# run
#
def run(dma330, pc):
	# check DMA330 status
	core = dma330["core"]["regs"]
	base = int(dma330["core"]["base"],16)
	
	addr = get_addr(core, base, "DBGSTATUS")
	while True:
		print("Read DMA330 status...")
		val = readreg(addr)
		if (val & 0x01)==0:	# DMA330 idle?
			break
		print("busy")
		time.sleep(0.1)
	print("ready to run")
	
	inst1 = (readb(pc-1) << 24) | (readb(pc-2) << 16) | (readb(pc-3) << 8) | readb(pc-4)
	inst0 = (readb(pc-5) << 24) | (readb(pc-6) << 16)
	# get channel number form DMAGO instruction
	ch = (inst0>>24)&0xFF
	if ch >= 0:
		v = ((ch&0x07) << 8) | 0x01
	else:
		# manage channel
		v = 0
	inst0 |= (v &0xFFFF)
	
	writereg(get_addr(core, base, "DBGINST0"),inst0)
	writereg(get_addr(core, base, "DBGINST1"),inst1)
	# start DMA
	print("Start DMA")
	writereg(get_addr(core, base, "DBGCMD"),0)
	
	#
	# check DMA status
	# 
	addr = get_addr(core, base, "DSR")
	while True:
		print("Read DSR...")
		val = readreg(addr)
		if (val & 0xF)==0:	# DMA330 stopped?
			break
		print("status = "+ str(hex(val)))
		time.sleep(0.1)
	# dump status registers
	dump_regs(ch, dma330["CH"+str(ch)])
	
	return
	
	
	
#
# parsing
#

def parse(line, base):
	l = line.replace('\n','').strip()
	if re.search("^;;",l):
		return base
	l = l.replace(',',' ').split(";;")
	l[0].strip()
	print(l[0])
	l = l[0].split()
	if len(l)==0:
		return base
	f = l.pop(0)
	if f in dma330_asm:
		inst = dma330_asm[f]
		if len(l) >= inst[2]:
			base = inst[0](base, l)
		else:
			print("arguments number not enough")
	else:
		print("Not found " + f)
		return base
	return base


#
# start main program
#
def main():
	global base
	#
	# try to open DMA330 assembly program file
	#
	try:
		file = sys.argv[1]
	except:
		file = input("Read file of DMA330 program:")
	
	try:
		ifd = open(file, 'r')
	except IOError:
		print ("Could not open read file \"", file,"\"")
		sys.exit()
	
	#
	# try to connect traget
	#
	try:
		HOST = sys.argv[2]
	except:
		HOST = input("Input host IP: ")
	# do connect HOST
	if not connect(HOST):
		return
	
	#
	# load cluster register file
	#
	#with open('dma330.json', 'r', encoding='utf-8') as f:
	#	dma330 = json.load(f)
	with open('dma_regs.json', 'r', encoding='utf-8') as f:
		dma330 = json.load(f)
	#
	# get current target s7_cm0.cpu or s7_cm4.cpu
	#
	t = targets(None)
	print("Target = " + t)
	
	# repeat read line from file
	pc = insts_base
	for line in ifd:
		pc = parse(line, pc)
		if pc < 0:
			break
	# run program
	if pc > 0:
		print("PC= " + hex(pc))
		run(dma330, pc)
		
	# close read file
	ifd.close()
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
