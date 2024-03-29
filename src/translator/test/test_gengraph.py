from __future__ import print_function
import re
import time
from datetime import timedelta
import sys
sys.path.append('../')
import egraph
import vgraph
from gengraph import gen_egraph
from gengraph import process
import timer


#
# uinit test
# test case: initial test vertex graph and add vertex
# show graph
#

#
# uinit test
# test case: initial test edeg graph and do convert to vertex graph
# show graph
#
g = egraph.eGraph()
g.add("OUTPUT_0",["OUTPUT_0","f_q2_N_13"])
g.add("OUTPUT_1",["OUTPUT_1","f_q2_N_14"])
g.add("f_q2_N_15",["DRLATN_9","f_q2_N_11","f_q2_N_12"]) # loop path
g.add("f_q2_N_13",["DRLATN_9","f_q2_N_11","f_q2_N_12"])
g.add("f_q2_N_14",["DRLATN_8","f_q2_N_7","f_q2_N_10"])
g.add("f_q2_N_12",["DRLATN_8","f_q2_N_7","f_q2_N_10"])	# loop path
g.add("f_q2_N_11",["DRLATN_6","f_q2_N_1","f_q2_N_6"])
g.add("f_q2_N_10",["DRLATN_7","f_q2_N_8","f_q2_N_9"])
g.add("f_q2_N_9",["DRLATN_5","f_q2_N_4","f_q2_N_5"])
g.add("f_q2_N_8",["DRLATN_4","f_q2_N_2","f_q2_N_3","f_q2_N_15"])
g.add("f_q2_N_7",["DRLATN_4","f_q2_N_2","f_q2_N_3","f_q2_N_15"])
g.add("f_q2_N_6",["DRLATN_4","f_q2_N_2","f_q2_N_3","f_q2_N_15"])
g.add("f_q2_N_5",["INUPT_4","fake_INPUT_4"])
g.add("f_q2_N_4",["INUPT_3","fake_INPUT_3"])
g.add("f_q2_N_3",["INUPT_2","fake_INPUT_2"])
g.add("f_q2_N_2",["INUPT_1","fake_INPUT_1"])
g.add("f_q2_N_1",["INUPT_0","fake_INPUT_0"])
#print(g)


vg = vgraph.vGraph()

keys = g.getkeys()
for k in keys:
	if re.search("^OUTPUT_",k):
		print("\nDFS search edge graph start from " + k)
		g.dfs(k, process, vg)

vg.show(None)


'''
data = [
['OUTPUT_0', 'OUTPUT_0', 'f_mac_out[7]', 'DRLATN_148', 'f_q2_N_7', 'DRLATR_149', 'f_q1_N_7', 'DRLATN_150', 'f_N16', 'TH24COMP_123', 'f_n1_N', 'TH24COMP_121', 't_mul_reg[7]', 'DRLATN_184', 't_q2_N_19', 'DRLATR_185', 'f_q1_N_19', 'DRLATN_186', 'f_N8', 'THAND0_52', 't_n53', 'THAND0_54', 't_n55', 'TH23_5', 't_n59', 'TH24COMP_110', 't_n1_N_2', 'TH24COMP_108', 'f_n50', 'THAND0_98', 'f_inb_reg[2]', 'DRLATN_193', 't_q2_N_22', 'DRLATR_194', 'f_q1_N_22', 'DRLATN_195', 'f_inb[2]', 'INPUT_9'],
['OUTPUT_0', 'OUTPUT_0', 'f_mac_out[7]', 'DRLATN_148', 'f_q2_N_7', 'DRLATR_149', 'f_q1_N_7', 'DRLATN_150', 'f_N16', 'TH24COMP_123', 'f_n1_N', 'TH24COMP_121', 't_mul_reg[7]', 'DRLATN_184', 't_q2_N_19', 'DRLATR_185', 'f_q1_N_19', 'DRLATN_186', 'f_N8', 'THAND0_52', 't_n53', 'THAND0_54', 't_n55', 'TH23_5', 't_n59', 'TH24COMP_110', 't_n1_N_2', 'TH24COMP_108', 'f_n50', 'THAND0_98', 'f_inb_reg[2]', 'DRLATN_193', 't_q2_N_22', 'DRLATR_194', 'f_q1_N_22', 'DRLATN_195', 't_inb[2]', 'INPUT_13'],
['OUTPUT_0', 'OUTPUT_0', 'f_mac_out[7]', 'DRLATN_148', 'f_q2_N_7', 'DRLATR_149', 'f_q1_N_7', 'DRLATN_150', 'f_N16', 'TH24COMP_123', 'f_n1_N', 'TH24COMP_121', 't_mul_reg[7]', 'DRLATN_184', 't_q2_N_19', 'DRLATR_185', 'f_q1_N_19', 'DRLATN_186', 'f_N8', 'THAND0_52', 't_n53', 'THAND0_54', 't_n55', 'TH23_5', 't_n59', 'TH24COMP_110', 't_n1_N_2', 'TH24COMP_108', 'f_n50', 'THAND0_98', 'f_inb_reg[2]', 'DRLATN_193', 't_q2_N_22', 'DRLATR_194', 't_q1_N_22', 'DRLATN_195', 'f_inb[2]', 'INPUT_9'],
['OUTPUT_0', 'OUTPUT_0', 'f_mac_out[7]', 'DRLATN_148', 'f_q2_N_7', 'DRLATR_149', 'f_q1_N_7', 'DRLATN_150', 'f_N16', 'TH24COMP_123', 'f_n1_N', 'TH24COMP_121', 't_mul_reg[7]', 'DRLATN_184', 't_q2_N_19', 'DRLATR_185', 'f_q1_N_19', 'DRLATN_186', 'f_N8', 'THAND0_52', 't_n53', 'THAND0_54', 't_n55', 'TH23_5', 't_n59', 'TH24COMP_110', 't_n1_N_2', 'TH24COMP_108', 'f_n50', 'THAND0_98', 'f_inb_reg[2]', 'DRLATN_193', 't_q2_N_22', 'DRLATR_194', 't_q1_N_22', 'DRLATN_195', 't_inb[2]', 'INPUT_13'],
['OUTPUT_0', 'OUTPUT_0', 'f_mac_out[7]', 'DRLATN_148', 'f_q2_N_7', 'DRLATR_149', 'f_q1_N_7', 'DRLATN_150', 'f_N16', 'TH24COMP_123', 'f_n1_N', 'TH24COMP_121', 't_mul_reg[7]', 'DRLATN_184', 't_q2_N_19', 'DRLATR_185', 'f_q1_N_19', 'DRLATN_186', 'f_N8', 'THAND0_52', 't_n53', 'THAND0_54', 't_n55', 'TH23_5', 't_n59', 'TH24COMP_110', 't_n1_N_2', 'TH24COMP_108', 'f_n50', 'THAND0_98', 'f_ina_reg[3]', 'DRLATN_208', 'f_q2_N_27', 'DRLATR_209', 'f_q1_N_27', 'DRLATN_210', 'f_ina[3]', 'INPUT_16'],
['OUTPUT_0', 'OUTPUT_0', 'f_mac_out[7]', 'DRLATN_148', 'f_q2_N_7', 'DRLATR_149', 'f_q1_N_7', 'DRLATN_150', 'f_N16', 'TH24COMP_123', 'f_n1_N', 'TH24COMP_121', 't_mul_reg[7]', 'DRLATN_184', 't_q2_N_19', 'DRLATR_185', 'f_q1_N_19', 'DRLATN_186', 'f_N8', 'THAND0_52', 't_n53', 'THAND0_54', 't_n55', 'TH23_5', 't_n59', 'TH24COMP_110', 't_n1_N_2', 'TH24COMP_108', 'f_n50', 'THAND0_98', 'f_ina_reg[3]', 'DRLATN_208', 'f_q2_N_27', 'DRLATR_209', 'f_q1_N_27', 'DRLATN_210', 't_ina[3]', 'INPUT_20'],
['OUTPUT_0', 'OUTPUT_0', 'f_mac_out[7]', 'DRLATN_148', 'f_q2_N_7', 'DRLATR_149', 'f_q1_N_7', 'DRLATN_150', 'f_N16', 'TH24COMP_123', 'f_n1_N', 'TH24COMP_121', 't_mul_reg[7]', 'DRLATN_184', 't_q2_N_19', 'DRLATR_185', 'f_q1_N_19', 'DRLATN_186', 'f_N8', 'THAND0_52', 't_n53', 'THAND0_54', 't_n55', 'TH23_5', 't_n59', 'TH24COMP_110', 't_n1_N_2', 'TH24COMP_108', 'f_n50', 'THAND0_98', 'f_ina_reg[3]', 'DRLATN_208', 'f_q2_N_27', 'DRLATR_209', 't_q1_N_27', 'DRLATN_210', 'f_ina[3]', 'INPUT_16'],
['OUTPUT_0', 'OUTPUT_0', 'f_mac_out[7]', 'DRLATN_148', 'f_q2_N_7', 'DRLATR_149', 'f_q1_N_7', 'DRLATN_150', 'f_N16', 'TH24COMP_123', 'f_n1_N', 'TH24COMP_121', 't_mul_reg[7]', 'DRLATN_184', 't_q2_N_19', 'DRLATR_185', 'f_q1_N_19', 'DRLATN_186', 'f_N8', 'THAND0_52', 't_n53', 'THAND0_54', 't_n55', 'TH23_5', 't_n59', 'TH24COMP_110', 't_n1_N_2', 'TH24COMP_108', 'f_n50', 'THAND0_98', 'f_ina_reg[3]', 'DRLATN_208', 'f_q2_N_27', 'DRLATR_209', 't_q1_N_27', 'DRLATN_210', 't_ina[3]', 'INPUT_20'],
['OUTPUT_0', 'OUTPUT_0', 'f_mac_out[7]', 'DRLATN_148', 'f_q2_N_7', 'DRLATR_149', 'f_q1_N_7', 'DRLATN_150', 'f_N16', 'TH24COMP_123', 'f_n1_N', 'TH24COMP_121', 't_mul_reg[7]', 'DRLATN_184', 't_q2_N_19', 'DRLATR_185', 'f_q1_N_19', 'DRLATN_186', 'f_N8', 'THAND0_52', 't_n53', 'THAND0_54', 't_n55', 'TH23_5', 't_n59', 'TH24COMP_110', 't_n1_N_2', 'TH24COMP_108', 'f_n50', 'THAND0_98', 'f_ina_reg[3]', 'DRLATN_208', 't_q2_N_27', 'DRLATR_209', 'f_q1_N_27', 'DRLATN_210', 'f_ina[3]', 'INPUT_16'],
]
vg = vgraph.vGraph()
id = 0

def process(n, l):
	global vg
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

for i in data:
	process(id,i)
print(vg)
'''
'''
def show_progress(g, start_time):
	count = g.getcount()
	elapsed_time = time.time() - start_time
	print(str(timedelta(seconds=int(elapsed_time))),end="")
	print(" process number = " + str(count),end="\r")
	return

# try to open read file
if len(sys.argv) <= 1:
	print ("gengraph.py <inputfile>")
	sys.exit()



g = gen_egraph(sys.argv[1])
if g:
	#print(g)
	#print("\n")
	g.clear()
	
	print("\nWrite vertex graph into file")
	fname = input("input filename:")
	try:
		ofd0 = open(fname, "w+")
	except:
		print ("Could not open write file \"" + fname + "\"")
		sys.exit()
	
	print("\nWrite invert vertex graph into file")
	fname = input("input filename:")
	try:
		ofd1 = open(fname, "w+")
	except:
		print ("Could not open write file \"" + fname + "\"")
		sys.exit()
		
	vg = vgraph.vGraph()
	start_time = time.time()
	t = timer.RepeatTimer(1, show_progress, [g, start_time])
	# start timer
	t.start()
	keys = g.getkeys()
	for k in keys:
		if re.search("^OUTPUT_",k):
			print("\nDFS search edge graph start from " + k)
			g.dfs(k, process, vg)
			#print(vg)
	# stop timer
	t.cancel()
	print("\n")
	
	# show vertex graph
	vg.show(ofd0)
	
	# invert vgraph
	ivg = vg.invert()
	
	# show invert vertex graph
	ivg.show(ofd1)
	try:
		ofd0.close
	except:
		pass
		
	try:
		ofd1.close
	except:
		pass
	#	
	# list search path
	#
	keys = vg.getkeys()
	for k in keys:
		if re.search("^OUTPUT_",k):
			print("\nDFS search vertex graph start from " + k)
			vg.dfs(k, None, None)
else:
	print("cannot create graph, exit")
'''

'''
from gengraph import add_netdb

line="bufnet_1=INV4X_637(ackin)"

g = egraph.eGraph()

add_netdb(line, g)
'''
