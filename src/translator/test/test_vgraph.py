import sys
import re
sys.path.append('../')
import vgraph
#
# unit test
# test case: initial test vertex graph and add vertex
# show graph
#	addneighbor rule: v.addneighbor("Y","X") input line number X from neighbor node Y

g = vgraph.vGraph()

g.add("OUTPUT_0")
v = g.getvertex("OUTPUT_0")
v.addneighbor("N9","L13")

g.add("OUTPUT_1")
v = g.getvertex("OUTPUT_1")
v.addneighbor("N8","L14")

g.add("N10")
v = g.getvertex("N10")
v.addneighbor("N5","L15")

g.add("N9")
v = g.getvertex("N9")
v.addneighbor("N6","L11")

g.add("N8")
v = g.getvertex("N8")
v.addneighbor("N7","L10")
v.addneighbor("N4","L7")
v.addneighbor("N10","L16")

g.add("N7")
v = g.getvertex("N7")
v.addneighbor("N4","L8")
v.addneighbor("N5","L9")

g.add("N6")
v = g.getvertex("N6")
v.addneighbor("INPUT_0","L1")
v.addneighbor("N4","L6")

g.add("N5")
v = g.getvertex("N5")
v.addneighbor("INPUT_3","L4")
v.addneighbor("INPUT_4","L5")

g.add("N4")
v = g.getvertex("N4")
v.addneighbor("INPUT_1","L2")
v.addneighbor("INPUT_2","L3")

g.add("INPUT_0")
g.add("INPUT_1")
g.add("INPUT_2")
g.add("INPUT_3")
g.add("INPUT_4")



print("==== Original graph ====")
print(len(g))
print(g)
#g.show(None)

'''
print("Write vertex graph into file")
fname = input("input filename:")
try:
	ofd = open(fname, "w+")
except:
		print ("Could not open write file \"" + fname + "\"")
		sys.exit()
# write graph into file		
g.show(ofd)

try:
	ofd.close
except:
	pass
'''	
'''
print("==== Do DFS search path from OUTPUT_x ====")
g.cleartrace()
g.dfs("OUTPUT_0",None,None)
print(g.gettrace())
g.cleartrace()
g.dfs("OUTPUT_1", None, None)
print(g.gettrace())
'''

'''
print("==== Invert graph ====")
ig = g.invert()
#ig.show(None)
#print(ig)
ig.bfs("^INPUT_", None, None)
ig.show(None)
'''
'''
print("==== BFS search adn draw color ====")
keys = g.getkeys()
for k in keys:
	if re.search("^INPUT_",k):
		#ig.cleartrace()
		ig.bfs(k, None, None)
		#print(ig.gettrace())
#ig.show(None)
'''

'''		
ig.cleartrace()
ig.bfs("INPUT_0")
print(ig.gettrace())

ig.cleartrace()
ig.bfs("INPUT_1")
print(ig.gettrace())

ig.cleartrace()
ig.bfs("INPUT_2")
print(ig.gettrace())

ig.cleartrace()
ig.bfs("INPUT_3")
print(ig.gettrace())

ig.cleartrace()
ig.bfs("INPUT_4")
print(ig.gettrace())
'''


'''
g.cleartrace()
ig.dfs("INPUT_0", None, None)
print(g.gettrace())

g.cleartrace()
ig.dfs("INPUT_1", None, None)
print(g.gettrace())

g.cleartrace()
ig.dfs("INPUT_2", None, None)
print(g.gettrace())

g.cleartrace()
ig.dfs("INPUT_3", None, None)
print(g.gettrace())

g.cleartrace()
ig.dfs("INPUT_4", None, None)
print(g.gettrace())
'''
#
# test case:  do DFS search graph and show result
#
'''
def show_trace(l):	
	for i in l:
		n = l.pop()
		while(len(n)):
			v = n.pop()
			if re.search("^OUTPUT_[0-9]",v) or \
				re.search("^INPUT_[0-9]",v):
				print("->" + v,end="")
				pass
			else:
				print(v,end="")
				if len(n)>1:
					print("->",end="")
		print("\n")
'''		
#	
# Search keys to find initial point (INPUT_XXX) or (OUTPUT_XXX) X is number 0-9
#
'''
keys = g.getkeys()
for k in keys:
	if re.search("^OUTPUT_[0-9]",k):
		g.dfs(k, None, None)
'''		
#
# test case:  invert graph, i.e. change initial point from OUTPUT_[0-9] to INPUT_[0-9]
#
'''
print("\nInvert Graph")
ig = g.invert()
ig.show()

print("\nInvert Graph again")
g2 = ig.invert()
g2.show()
'''
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

#
# test case:  create vertex graph from edge graph
#
'''
import egraph
import re
g = egraph.eGraph()
g.add("OUTPUT_0",["OUTPUT_0","L13"])
g.add("OUTPUT_1",["OUTPUT_1","L14"])
g.add("L13",["T9","L11"])
g.add("L14",["T8","L7","L10"])
g.add("L11",["N6","L1","L6"])
g.add("L10",["N7","L8","L9"])
g.add("L8",["T4","L2","L3"])
g.add("L9",["N5","L4","L5"])
g.add("L7",["N4","L2","L3"])
g.add("L6",["N4","L2","L3"])
g.add("L5",["INUPT_4","INPUT_4"])
g.add("L4",["INUPT_3","INPUT_3"])
g.add("L3",["INUPT_2","INPUT_2"])
g.add("L2",["INUPT_1","INPUT_1"])
g.add("L1",["INUPT_0","INPUT_0"])

#print(g)

vg = vGraph()
keys = g.getkeys()
for k in keys:
	if re.search("^OUTPUT",k):
		g.cleartrace()
		g.dfs(k)
		l = g.gettrace()
		for i in l:
			print(i)
			
			i.pop(0) # virtual output line
			n = i.pop(0)	# head node OUTPUT
			print("add vertex:" + n + " ",end="")
			vg.add(n)
			v = vg.getvertex(n)
			add_to_edge = 0
			while(i):
				if not add_to_edge:
					e = i.pop(0) # get edge
					n = i.pop(0) # get node
				else:
					e += "+" + i.pop(0) # get edge
					n = i.pop(0) # get node
				if re.search("^T", n):
					add_to_edge =1
					e += "+" + n
					continue
				print("add neighbor " + n +" edge " + e)
				add_to_edge = 0
				v.addneighbor(n,e)
				print("add vertex:" + n + " ", end="")
				vg.add(n)
				v = vg.getvertex(n)
				print("--end--")
	
			
print("\n === Vertex graph ===")
print(vg)

keys = vg.getkeys()
print(keys)
for k in keys:
	if re.search("^OUTPUT_[0-9]",k):
		vg.dfs(k)
		show_trace(vg.gettrace())
		vg.cleartrace()
'''		
