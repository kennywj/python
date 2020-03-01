#
# class for keep netlist information
#
from __future__ import print_function
import re
import sys
import egraph
import vgraph

index = 0
input_id = 0
output_id = 0

#
# function: add_netdb
# parsing "INPUT(f_coef[3])" into INPUT and f_coef[3] and then put f_coef[3] as key, INPUT into list
# i.e input line as key and output lines as edges
#
def add_netdb(line, db):
	e = []
	#ignore ack line
	if re.search('^ack',line):
		print("ignore : " + line)
	elif re.search('^OUTPUT',line):
		# OUTPUT(xxx) ==> add virtual line "OUTPUT_xxx as keys, xxx as input line to other (edge)
		line = line.replace('(', ' ').replace(')', '').replace('\n','')
		value = line.split(' ',1)[0]
		key = line.split(' ',1)[-1]
		if re.search('^ack',key):
			print("ignore : " + line)
			pass
		else:
			value += "_" + str(output_id)
			# add list[0] vetex
			e.append(value)
			# add list[1] input line edge
			e.append(key)
			#print("key= "+ key + ", vertex= " + value + ", virtual output line= ", value + "_" + key)
			global output_id
			db.add(value, e)
			output_id += 1
	elif re.search('^INPUT',line):
		# INPUT(xxx) ==> add xxx as key, virtual line "INPUT_xxx" as ouput line to other (edge)
		line = line.replace('(', ' ').replace(')', '').replace('\n','')
		value = line.split(' ',1)[0]
		key = line.split(' ',1)[-1]
		if re.search('^ack',key):
			print("ignore : " + line)
			pass
		else:
			global input_id
			value += "_" + str(input_id)
			# add list[0] vetex
			e.append(value)
			# add list[1] output virtual line
			global input_id
			e.append(value)
			input_id += 1
			#print("key= "+ key + ", vertex= " + value + ", virtual output line= ", value + "_" + key)
			db.add(key, e)
	else:
		# split string "XXX=AAA(VVV,LLL,...)" into key = XXX, value = ["VVV","LLL",...]
		key = line.split('=',1)[0]
		value = line.split('=',1)[-1]
		key = key.replace('(', ' ').replace(')', '').strip()
		key = key.split(',')
		value = value.replace('(', ',').replace(')', '').strip().split(',')
		
		# check if element only vertex but without input lines
		if not value[1]:
			# remove empty string and add virtual line
			value.remove(value[1])
			value.append("INPUT_"+value[0])
		
		global index
		# append each vertex unique index, ignore ackXXX	
		value[0] = value[0]+'_'+str(index)
		index += 1
		for v in value:
			if re.search('^ack',v):
				pass
			else:
				e.append(v)
		# add list elements into graph database
		for k in key:
			db.add(k, e)
	return
#
# generate edge graph
#
def gen_egraph(file):
	data = ""
	print("\nDo generate graph...");
	# try to open read file
	try:
		ifd = open(file, "r")
	except IOError:
		print ("Could not open read file \"", file,"\"")
		return
	# initial a graph
	g = egraph.eGraph()
	index = 0
	input_id = 0
	output_id = 0
	# repeat read line from file
	for line in ifd:
		add_netdb(line, g)
	# close read file
	ifd.close()
	return g
	
#
# handle the egraph dfs result. put in vgraph
#	
def process(vg, l):
	e=""		# edges string
	l.pop(0) # pop virtual line, not add to edges
	n = l.pop(0) # head node
	vg.add(n)
	v = vg.getvertex(n)
	while(l):
		if e:
			e += "+"
		e += l.pop(0) # eage to neighbor
		n = l.pop(0) # neighbor
		if re.match("^DRLAT[R|N]",n) or \
			re.match("^INPUT",n):
			v.addneighbor(n,e)
			e=""
			vg.add(n)
			v = vg.getvertex(n)
		else:
			e += "+" + n
	return	