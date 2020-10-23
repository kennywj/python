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

def do_generate(item, data, weight):
    # calculate test data file size
    channel_num = item["channel_num"]
    high = item["feature_map_high"]
    width = item["feature_map_width"]
    total = high * width * channel_num
    try:
        fd = open(item["data"], "wb")
    except:
        print("open file " + item["data"] + "fail")
        return
    while total > 0:
        fd.write(data.to_bytes(1, 'little')) 
        total -=1
    fd.close()
    
    kernel =  find_index(item["kernel"],["3x3","1x1"])
    kernel_num = item["kernel_num"]
    if kernel==0: # 3x3
        total = 3 * 3 * kernel_num
    else:
        total = kernel_num
    try:
        fd = open(item["weight"], "wb")
    except:
        print("open file " + item["weight"] + "fail")
        return
    while total > 0:
        fd.write(weight.to_bytes(1, 'little')) 
        total -=1
    fd.close()
    return

def main():
    #
    # try to open register JSON file
    #
    try:
        file = sys.argv[1]
    except:	
        file = input("Read file of test case:")
    #
    # open test case JSON file
    #
    with open(file, 'r', encoding='utf-8') as f:
        output = json.load(f)
    #    
    # input test data pattern and weight pattern
    #
    data = query_value("data pattern: ", 0, 255)
    weight = query_value("weight pattern: ", 0, 255)
    #
    # To generate test data file and weight file
    #
    keys = output.keys()
    for i in keys:
        do_generate(output[i], data, weight)
        
    return


# start program
if __name__ == '__main__':
	main()