from __future__ import print_function
import re
import sys
sys.path.append('../')
import egraph

#
# uinit test
# test case: initial test graph and show graph
# give virtual line OUTPUT_[0-9], INPUT_[0-9]
#


def show_trace(n, l):
	print("path ("+ str(n)+ "):", end="")
	while(l):
		print(l.pop(0),end='')
		if len(l)!=0:
			print("->",end="")
	print('\n')


#
# uinit test
# test case: initial test vertex graph and add vertex
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

#print("===> Original Graph")
#print(g)

print("===> Do DSF trace Graph")
keys = g.getkeys()
for k in keys:
	if re.search("^OUTPUT_[0-9]",k):
		# do DFS
		#g.dfs(k, None)
		g.dfs(k, None, None)
		#show_trace(g.gettrace())
		#g.cleartrace()

#
# test case:  do BFS search graph and show result
# Search keys to find initial point (INPUT_XXX) or (OUTPUT_XXX) X is number 0-9
#
'''
print("===> Do BSF trace Graph")
keys = g.getkeys()
for k in keys:
	if re.search("^OUTPUT_[0-9]",k) or \
		re.search("^INPUT_[0-9]",k):
		# do BFS
		g.bfs(k)
		show_trace(g.gettrace())
		g.cleartrace()
'''
#
# test case:  invert graph, i.e. change initial point from OUTPUT_[0-9] to INPUT_[0-9]
#
'''
print("\nInvert Graph")
ig = g.invert()
print(ig)
'''
#print("\nInvert Graph again")
#g2 = ig.invert()
#g2.show()

#
# test case:  do BFS search graph and show result
#
'''
keys = g.getkeys()
#print(keys)
for k in keys:
	if re.search("^INPUT_[0-9]",k) or \
		re.search("^OUTPUT_[0-9]",k):
		g.bfs(k)
		show_trace(g.gettrace())
		g.cleartrace()
'''
