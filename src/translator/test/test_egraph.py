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
g.add("OUTPUT_0",["OUTPUT_0","L13"])
g.add("OUTPUT_1",["OUTPUT_1","L14"])
g.add("L15",["N9","L11","L12"]) # loop path
g.add("L13",["N9","L11","L12"])
g.add("L14",["N8","L7","L10"])
g.add("L12",["N8","L7","L10"])	# loop path
g.add("L11",["N6","L1","L6"])
g.add("L10",["N7","L8","L9"])
g.add("L9",["N5","L4","L5"])
g.add("L8",["N4","L2","L3","L15"])
g.add("L7",["N4","L2","L3","L15"])
g.add("L6",["N4","L2","L3","L15"])
g.add("L5",["INUPT_4","fake_INPUT_4"])
g.add("L4",["INUPT_3","fake_INPUT_3"])
g.add("L3",["INUPT_2","fake_INPUT_2"])
g.add("L2",["INUPT_1","fake_INPUT_1"])
g.add("L1",["INUPT_0","fake_INPUT_0"])

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
