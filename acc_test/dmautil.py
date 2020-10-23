#
# utility functions
#
#!/usr/bin/python
# -*- coding: utf-8 -*-

from utility import *

loopforever = []
loopstart = []

def DMAADDH(addr, l):
	if l[0] == "SAR":
		r = 0x00
	elif l[0] == "DAR":
		r = 0x01
	else:
		print("paramter error")
		return -1
	if re.search("^0x",l[1]):
		v = int(l[1],16) & 0xFFFF
	else:
		v = int(l[1]) & 0xFFFF
	writeb(addr, (0x54 | r))
	writeb(addr+1, v&0xFF)
	writeb(addr+2, (v>>8)&0xFF)
	return addr+3

def DMAANDH(addr, l):
	if l[0] == "SAR":
		r = 0x00
	elif l[0] == "DAR":
		r = 0x01
	else:
		print("paramter error")
		return -1
	if re.search("^0x",l[1]):
		v = int(l[1],16) & 0xFFFF
	else:
		v = int(l[1]) & 0xFFFF
	writeb(addr, (0x5C | r))
	writeb(addr+1,v&0xFF)
	writeb(addr+2,(v>>8)&0xFF)
	return addr+3

def DMAEND(addr, l):
	writeb(addr, 0)
	return addr+1

def DMAFLUSHP(addr, l):
	i = int(l[0])
	i = (i&0xFF)<< 3
	writeb(addr, 0x35)
	writeb(addr+1,i)
	return addr+2

def DMAGO(addr, l):
	c = int(l[0][1:]) & 0x07
	v = int(l[1],16)
	if len(l)>=2:
		s = 0x01<<1
	else:
		s = 0x00
	writeb(addr, (0xA0|s))
	writeb(addr+1, c)
	writeb(addr+2,v&0xFF)
	writeb(addr+3,(v>>8)&0xFF)
	writeb(addr+4,(v>>16)&0xFF)
	writeb(addr+5,(v>>24)&0xFF)
	return addr+6
	
def DMAKILL(addr, l):
	writeb(addr,0x01)
	return addr+1

def DMALDS(addr, l):
	writeb(addr, 0x05)
	return addr+1
	
def DMALDB(addr, l):
	writeb(addr, 0x07)
	return addr+1
	
def DMALD(addr, l):
	writeb(addr, 0x04)
	return addr+1
	
def DMALDPS(addr, l):
	i = int(l[0])
	i=(i&0x1F)<<3
	writeb(addr, 0x25)
	writeb(addr+1, i)
	return addr+2

def DMALDPB(addr, l):
	i = int(l[0])
	i=(i&0x1F)<<3
	writeb(addr, 0x27)
	writeb(addr+1, i)
	return addr+2

def DMALP(addr, l):
	if l[0]=="lc0":
		ch = 0
	elif l[0]== "lc1":
		ch = (0x01<<1)
	else:
		print("error argument")
		return -1
	lc = int(l[1])-1
	lc = lc&0xFF
	writeb(addr, 0x20|ch)
	writeb(addr+1, lc)
	loopforever.append(0) 
	#loopstart.append((addr+2)&0xFF)
	loopstart.append(addr+2)
	return addr+2

def DMALPFE(addr, l):
	loopforever.append(1)
	#loopstart.append(addr&0xFF)
	loopstart.append(addr)
	return addr

def DMALPEND(addr, l):
	if l[0]=="lc0":
		lc = 0
	elif l[0]=="lc1":
		lc = 1
	else:
		print("argument error")
		return -1
	if loopforever[-1]:
		lc = 0x01<<2
		nf = 0
	else:
		lc = (lc&0x01)<<2
		nf = (0x01)<<4
	writeb(addr, 0x28|lc|nf)
	writeb(addr+1, (addr-loopstart[-1]))
	loopforever.pop()
	loopstart.pop()
	return addr+2
	
def DMALPENDS(addr, l):
	if l[0]=="lc0":
		lc = 0
	elif l[0]=="lc1":
		lc = 1
	else:
		print("argument error")
		return -1
	if loopforever[-1]:
		lc = (0x01<<2)
		nf = 0
	else:
		lc = (lc&0x01)<<2
		nf = (0x01<<4)
	writeb(addr, 0x29|lc|nf)
	writeb(addr+1, (addr-loopstart[-1]))
	loopforever.pop()
	loopstart.pop()
	return addr+2
	
def DMALPENDB(addr, l):
	if l[0]=="lc0":
		lc = 0
	elif l[0]=="lc1":
		lc = 1
	else:
		print("argument error")
		return -1
	if loopforever[-1]:
		lc = 0x01<<2
		nf = 0
	else:
		lc = (lc&0x01)<<2
		nf = (0x01)<<4
	writeb(addr, 0x2B|lc|nf)
	writeb(addr+1, (addr-loopstart[-1]))
	loopforever.pop()
	loopstart.pop()
	return addr+2


#
# parsing CCR arguments
#
size2bits={"8":0,"16":1,"32":2,"64":3,"128":4,"256":5}

def DMACCR(l):
	src_addr_inc = 1
	src_burst_size = 8
	src_burst_len = 1
	src_protect = 2
	src_cache=0
	dst_addr_inc = 1
	dst_burst_size = 8
	dst_burst_len = 1
	dst_protect = 2
	dst_cache=0
	endian_swap_size = 0
	# parsing aruments
	for i in l:
		if i.find("SA")==0:
			if i[2:]=="I":
				src_addr_inc = 1
			elif i[2:]=="F":
				src_addr_inc = 0
			else:
				print("unknow parameters: " + i)
				return -1
			#print("src_addr_inc = "+str(src_addr_inc))
		elif i.find("SS")==0:
			src_burst_size = size2bits[i[2:]]
			#print("src_burst_size = "+str(src_burst_size))
		elif i.find("SB")==0:
			src_burst_len = int(i[2:])-1
			#print("src_burst_len = " + str(src_burst_len))
		elif i.find("SP")==0:
			src_protect = int(i[2:])
			#print("src_protect = " + str(src_protect))
		elif i.find("SC")==0:
			src_cache=int(i[2:])
			#print("src_cache = " + str(src_cache))
		elif i.find("DA")==0:
			if i[2:]=="I":
				dst_addr_inc = 1
			elif i[2:]=="F":
				dst_addr_inc = 0
			else:
				print("unknow parameters: " + i)
				return -2
			#print("dst_addr_inc = " + str(dst_addr_inc))
		elif i.find("DS")==0:
			dst_burst_size = size2bits[i[2:]]
			#print("dst_burst_size = " + str(dst_burst_size))
		elif i.find("DB")==0:
			dst_burst_len = int(i[2:])-1
			#print("dst_burst_len = " + str(dst_burst_len))
		elif i.find("DP")==0:
			dst_protect = int(i[2:])
			#print("dst_protect = " + str(dst_protect))
		elif i.find("DC")==0:
			dst_cache = int(i[2:])
			#print("dst_cache = " + str(dst_cache))
		elif i.find("ES")==0:
			endian_swap_size = size2bits[i[2:]]
			#print("endian_swap_size = " + str(endian_swap_size))
		else:
			print("unknow parameters: " + i)
			return -3
			
	return ((endian_swap_size&0x07)<<28) |	\
			((dst_cache&0x07)<<25)  |	\
			((dst_protect&3)<<22) |		\
			((dst_burst_len&0xF)<<18) |	\
			((dst_burst_size&0xF)<<15)|	\
			((dst_addr_inc&0x01)<<14) |	\
			((src_cache&0x07)<<11)	|	\
			((src_protect&3)<<8) | 		\
			((src_burst_len&0xF)<<4) |	\
			((src_burst_size&0x7)<<1) |	\
			(src_addr_inc&0x01)
	
def DMAMOV(addr, l):
	if l[0] == "SAR":
		rd = 0x00
		v = int(l[1],16)
	elif l[0] == "CCR":
		rd = 0x01
		l.pop(0)
		v = DMACCR(l)
		if v < 0:
			print("DMAMOV:argument error 1")
			return -1
		#print("CCR argument = "+str(hex(v)))
	elif l[0] == "DAR":
		rd = 0x02
		v = int(l[1],16)
	else:
		print("DMAMOV:argument error 2")
		return -1
	
	writeb(addr, 0xBC)
	writeb(addr+1, rd)
	writeb(addr+2,v&0xFF)
	writeb(addr+3,(v>>8)&0xFF)
	writeb(addr+4,(v>>16)&0xFF)
	writeb(addr+5,(v>>24)&0xFF)
	return addr+6

def DMANOP(addr, l):
	writeb(addr, 0x18)
	return addr+1
	
def DMARMB(addr, l):
	writeb(addr, 0x12)
	return addr+1
	
def DMASEV(addr, l):
	# event argument is e? ? is 0~31
	i = int(l[0][1:])
	i=(i&0x1F)<<3
	writeb(addr, 0x34)
	writeb(addr+1, i)
	return addr+2
	
def DMASTB(addr, l):
	writeb(addr, 0xB)
	return addr+1
	
def DMASTS(addr, l):
	writeb(addr, 0x9)
	return addr+1
	
def DMAST(addr, l):
	writeb(addr, 0x8)
	return addr+1
	
def DMASTPS(addr, l):
	i = int(l[0])
	i=(i&0x1F)<<3
	writeb(addr, 0x29)
	writeb(addr+1, i)
	return addr+2
	
def DMASTPB(addr, l):
	i = int(l[0])
	i=(i&0x1F)<<3
	writeb(addr, 0x2B)
	writeb(addr+1, i)
	return addr+2
	
def DMASTZ(addr, l):
	writeb(addr, 0xC)
	return addr+1
	
def DMAWFE(addr, l):
	e = int(l[0])
	n = int(l[1])
	e=(e&0x1F)<<3
	writeb(addr, 0x36)
	if n:
		writeb(addr+1, e|0x02)
	else:
		writeb(addr+1, e)
	return addr+2
	
def DMAWFP(addr, l):
	i = int(l[0])
	i=(i&0x1F)<<3
	if l[1]=="single":
		tp = 0x18
	elif l[1]=="burst":
		tp = 0x1A
	elif l[1]=="peri":
		tp = 0x19
	else:
		print("error argument")
		return -1
	writeb(addr,tp)
	writeb(addr+1, i)
	return addr+2
	
def DMAWMB(addr, l):
	writeb(addr, 0x13)
	return addr+1
	

	
#
#	dma330 assembler dictionary
#	{key:[func, instruction length, argumenst number]}
#	
dma330_asm = {
	"DMAADDH":[DMAADDH,3,2],
	"DMAANDH":[DMAANDH,3,2],
	"DMAEND": [DMAEND,1,0],
	"DMAFLUSHP":[DMAFLUSHP,2,1],
	"DMAGO":[DMAGO,6,2],
	"DMAKILL":[DMAKILL,1,0],
	"DMALDS":[DMALDS,1,0],
	"DMALDB":[DMALDB,1,0],
	"DMALD":[DMALD,1,0],
	"DMALDPS":[DMALDPS,2,1],
	"DMALDPB":[DMALDPB,2,1],
	"DMALP":[DMALP,2,2],
	"DMALPEND":[DMALPEND,2,0],
	"DMALPENDS":[DMALPENDS,2,0],
	"DMALPENDB":[DMALPENDB,2,0],
	"DMALPFE":[DMALPFE,1,0],
	"DMAMOV":[DMAMOV,6,2],
	"DMANOP":[DMANOP,1,0],
	"DMARMB":[DMARMB,1,0],
	"DMASEV":[DMASEV,2,1],
	"DMASTB":[DMASTB,1,0],
	"DMASTS":[DMASTS,1,0],
	"DMAST":[DMAST,1,0],
	"DMASTPB":[DMASTPB,2,1],
	"DMASTPS":[DMASTPS,2,1],
	"DMASTZ":[DMASTZ,1,0],
	"DMAWFE":[DMAWFE,2,2],
	"DMAWFP":[DMAWFP,2,2],
	"DMAWMB":[DMAWMB,1,0]
}
