#
# utility functions
#
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import telnetlib
import time

tn=None
debug=True

#
# debug status
#
def debug_stat():
	return debug
#
# debug flag
#
def debug_en(flag):
    global debug
    debug=flag
    return
#
# genernate row/col number by kernel size
#
def get_num(kernel, num):
    if kernel==0:   # 3x3
        return num * 3
    else:
        return num
#
# generate register address by key
#
def get_addr(regbase, base, reg):
    offset = int(regbase[reg]["offset"],16)
    return base + offset


#
# Reset PA/cluster 
#
def do_reset(cluster, cluster_base):
	print("Do software reset PA...")
	addr = get_addr(cluster, cluster_base, "pa_control")
	control = 0x00020002
	writereg(get_addr(cluster, cluster_base, "pa_control"),control)
	control = 0x00000000
	writereg(get_addr(cluster, cluster_base, "pa_control"),control)
	time.sleep(0.1)
	
	print("Do reset cluster...")
	addr = get_addr(cluster, cluster_base, "cluster_control")
	control = 0x0000000C
	writereg(get_addr(cluster, cluster_base, "cluster_control"),control)
	control = 0x00000008
	writereg(get_addr(cluster, cluster_base, "cluster_control"),control)
	time.sleep(0.1)

	print("Reset Done.")
	return
    
#
# function: connect
#   input: remote Telenet server
#   output: None
#
def connect(HOST):
    global tn
    try:
        tn = telnetlib.Telnet(HOST, 4444)
        #tn.set_debuglevel(2)
        tn.read_until(b">")
        return True
    except IOError:
        print("Connect to " + HOST + " fail")
        return False

#
# function: disconnect
#   input: None
#   output: None
#
def disconnect():
	global tn
	if tn:
		tn.write(b"exit\n")
		print(tn.read_all().decode('ascii'))
		tn.close()
	return
    
#
# function: read register 
#   input: register address
#   output: contain of register
#
def readreg(reg):
	global tn, debug
	cmd = "mdw " + hex(reg) + "\r\n"
	tn.write(cmd.encode('ascii'))
	tn.read_until(b"\r\n")  #read command echo
	val = tn.read_until(b"\r\n").decode('ascii')
	v = val.split(':',2)[-1].strip()
	if debug:
		print("   read " + hex(reg) + "=0x" + v[2:].zfill(8))
	try:
		n = int(v,16)
	except ValueError:
		print("*** read register " + hex(reg) + " error, actual read = " + val)
		sys.exit(1)
	return n

#
# function: write register 
#   input: register address and value
#   output: none
#
def writereg(reg, val):
	global tn, debug
	if debug:
		print("   write " + hex(reg) + "=0x" + hex(val)[2:].zfill(8))
	cmd = "mww " + hex(reg) + " " + hex(val) + "\r\n"
	tn.write(cmd.encode('ascii'))
	tn.read_until(b"\r\n")  #read command echo
	return

#
# function: write byte to memory 
#   input: memory address and value
#   output: none
#
def writeb(addr, val):
	global tn, debug
	if debug:
		print("   write " + hex(addr) + "=0x" + hex(val)[2:].zfill(2))
	cmd = "mwb " + hex(addr) + " " + hex(val) + "\r\n"
	tn.write(cmd.encode('ascii'))
	tn.read_until(b"\r\n")  #read command echo
	return

#
# function: read byte from memory 
#   input: memory address
#   output: none
#
def readb(addr):
	global tn, debug
	cmd = "mdb " + hex(addr) + "\r\n"
	tn.write(cmd.encode('ascii'))
	tn.read_until(b"\r\n")  #read command echo
	val = tn.read_until(b"\r\n").decode('ascii')
	v = val.split(':',2)[-1].strip()
	if debug:
		print("   read " + hex(addr) + "=0x" + v.zfill(2))
	return int(v,16)

#	
# select targets
# 	
def targets(cpu):
	global tn
	if cpu:
		cmd = "targets "+ cpu + "\r\n"
		tn.write(cmd.encode('ascii'))
		tn.read_until(b"\r\n")  #read command echo
	# get current targets
	cmd = "target current\r\n"
	tn.write(cmd.encode('ascii'))
	tn.read_until(b"\r\n")  #read command echo
	return tn.read_until(b"\r\n").decode('ascii')
	

#	
# do_memtest
# 	
def do_memtest(base, size):
	global tn
	cmd = "runAllMemTests " + base + " " + size +"\r\n"
	#print(cmd)
	tn.write(cmd.encode('ascii'))
	while True:
		s = tn.read_until(b"\r\n").decode('ascii')
		print("   " + s, end = "")
		if s.find("All tests done")>=0:
			break
	return
	

#	
# do_set_remotetimeout
# 	
def do_set_remotetimeout(time):
	global tn
	cmd = "set remotetimeout " + str(time) +"\r\n"
	#print(cmd)
	tn.write(cmd.encode('ascii'))
	return	tn.read_until(b"\r\n").decode('ascii')
	
#
# function: bit filed 
#   input: mask list
#   output: new list
#
def bitmask(i, data):
    if i<97:
        m=int(i/32)
        n=int(i%32)
        if m<3:
            data[m] = data[m] & ~((1<<n)-1)
        
        while m>0:
            data[m-1]=0
            m-=1
    else:
        print("bitmask out of range: " + str(i))
    return data

# Ask a yes/no question via raw_input() and return their answer.
#
#   "question" is a string that is presented to the user.
#    "default" is the presumed answer if the user just hits <Enter>.
#        It must be "yes" (the default), "no" or None (meaning
#        an answer is required of the user).
#
#    The "answer" return value is True for "yes" or False for "no".
#
def query_yes_no(question, default="yes"):
    valid = {"yes": True, "y": True, "ye": True,
        "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            sys.stdout.write(default+"\r\n")
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
            "(or 'y' or 'n').\n")    

# Ask a question via input() and return their answer's index in list.
#
#   "question" is a string that is presented to the user.
#    The "option" are list of answer, return value is index of list element
#            
def query_string(question, option):
    while True:
        sys.stdout.write(question)
        s = input()
        if s:
            for i in option:
                if s == i:
                    return option.index(i)
        sys.stdout.write("Please give suitable option")
 
# Ask a question via input() and return their answer's index in list.
#
#   "question" is a string that is presented to the user.
#    The input value should between max value and min value, if not input, it should return min value
#  
def query_value(question, min, max):
    while True:
        sys.stdout.write(question)
        choice = input()
        if choice == '':
            sys.stdout.write(str(min)+"\r\n")
            return min
        else: 
            val = int(choice)
            if val >= min and val <= max:
                return val
            else:
                sys.stdout.write("Please give value between " + str(min) + " ~ " + str(max) +"\n")

#
# find key string in list
#
def find_index(key, option):
    for s in option:
        if key == s:
            return option.index(s)
    print(key + " not in ",end="")
    print(option)
    return -1                