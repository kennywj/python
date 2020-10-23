#
# test weight register functions
#
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import re
import json
import time
from utility import *

cluster_base = 0x40004000
pa_base  = 0x40004400
ifm_base = 0x20100000
ofm_base = 0x20130000
#
# push out weigh buffer
#
def push_weight(base, count):
    print("Write 0 to "+ str(hex(base+0x5c)) + " " + str(count) +" times to push weight data output")
    debug_en(False)
    while count>0:
        writereg(base+0x5c,0)
        count-=1
    debug_en(True)
    return
#
# read_weight
#
def read_weight(base, cluster):
    keys = cluster.keys()
    addr = 0
    debug_en(False)
    for i in keys:
        if re.match("^pa0_out_weight",i):
            val = readreg(base+addr)
            print("Read "+ i + " ("+ str(hex(base+addr))+") value= "+str(hex(val)))
            addr += 4 
    debug_en(True)
    return
    
#
# write_weight, 1 row 96 bytes, max 48 rows
#
def write_weight(base, data):
    addr = 0
    touch = 0
    debug_en(False)
    while len(data)>0:
        val = 0
        for s in range(4):
            if len(data):
                val = (val<<8) | data.pop(0)
            else:
                val = val<<8
        writereg(base+addr,val)
        print("Write " + str(hex(base+addr)) + ", val= " + str(hex(val)), end="")
        addr+=4
        if addr >= 96:
            addr = 0
            touch +=1
            print("->touch " + str(touch) + "\n")
        else:
            print("")
            
    if addr != 0:
        writereg(base+0x5c,0)
        touch += 1
        print("->touch " + str(touch) + "\n")
    debug_en(True)
    return touch


    
#
# start of test program
# usage: python3 weight_test.py <weight data> <HOST>]
#  
def main():
    #
    # try to open register JSON file
    #
    try:
        file = sys.argv[1]
    except:	
        file = input("Input file name of weight data:")
        
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
    with open('cluster.json', 'r', encoding='utf-8') as f:
        cluster = json.load(f)
        
    data =[]
    with open(file, 'rb') as f:
        while True:
            d = f.read(1)
            if not d:    # EOF?
                break
            data.append(int.from_bytes(d, "little"))
            
    # write 1 byte data to weight register, then push 48 times and check in weight out register
    #data =[1,2,3,4,5,6,7,8,9]
    size = len(data)
    print("Write " + str(size) + " data to weight input register")
    touch = write_weight(get_addr(cluster, cluster_base, "pa0_in_weight_3_0"), data)  
    push_weight(get_addr(cluster, cluster_base, "pa0_in_weight_3_0"), 48-touch)
    # repeat 
    while size > 0:
        print("Read data from weight output register")
        read_weight(get_addr(cluster, cluster_base, "pa0_out_weight_3_0"), cluster)
        size -= 96
    
    #
    # fill weight buffer and read 
    #
    '''
    data=[]
    for j in range(48):
        for i in range(96):
            data.append(j+1)
        print(data)
        write_weight(get_addr(cluster, cluster_base, "pa0_in_weight_3_0"), data)
        
    for j in range(48):
        print(j)
        read_weight(get_addr(cluster, cluster_base, "pa0_out_weight_3_0"), cluster)
    '''
    #read_weight(cluster, cluster_base)
    return
# start program
if __name__ == '__main__':
	main()