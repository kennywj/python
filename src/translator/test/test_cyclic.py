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
#v.addneighbor("N9","L17")	#loop path 1

g.add("N6")
v = g.getvertex("N6")
v.addneighbor("INPUT_0","L1")
v.addneighbor("N4","L6")
#v.addneighbor("N7","L18")	#loop path 2

g.add("N5")
v = g.getvertex("N5")
v.addneighbor("INPUT_3","L4")
v.addneighbor("INPUT_4","L5")
v.addneighbor("N8","L19")	# loop path 3

g.add("N4")
v = g.getvertex("N4")
v.addneighbor("INPUT_1","L2")
v.addneighbor("INPUT_2","L3")
v.addneighbor("N5","L20")	# loop path 4

g.add("INPUT_0")
g.add("INPUT_1")
g.add("INPUT_2")
g.add("INPUT_3")
g.add("INPUT_4")



print("==== Original graph ====")
#print(g)
g.show(None)

print("==== DFS search vgraph to detect loop ====")
g.cyclic_check("OUTPUT")
'''
keys = g.getkeys()
#print(keys)
for k in keys:
	if re.search("^OUTPUT_",k):
		print("key " + k)
		g.dfs(k, None, None)
'''
print("If graph is cyclic?", g.iscyclic())
