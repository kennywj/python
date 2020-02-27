from __future__ import print_function
import vertex
import stack
import re

class vGraph:
	# graph is a dictionary, key is in/out edge, data is vetex, color and out/in edge
	def __init__(self):
		self.items={}
		self.path=stack.Stack()
		return

	def add(self, k):
		# if node in vgraph database?
		if self.items.get(k):
			print("Vertex " + v + "exist")
			return
		else:
			# creat new node
			self.items[k] = vertex.Vertex()
		# set vertex node
		v = self.items[k]
		v.setname(k)
		return
		
	def getkeys(self):
		return self.items.keys()

	def getvertex(self, k):
		return self.items[k]
		
	def bfs(self,k):
		return
		
	def dfs(self,k):
		if not self.items.get(k):
			print("Vertex " + k + "not exist!")
			return
		# get vertex
		v = self.items[k]
		# puth this vertex
		self.path.push(k)
		#get neighbor list
		n = v.getneighbor()
		if not n:
			# neighbor is null, show path
			print(self.path)
		else:
			#for each neighbor in neighbor list, do DFS
			for i in n:
				self.dfs(i.getvertex())
		self.path.pop()
		return
		
	def invert(self):
		# invert direction grapy INPUT to OUTPUT /OUTPUT to INPUT
		# create a new graph
		g = vGraph()
		keys = self.items.keys()
		for k in keys:
			vertex = self.items[k]
			for n in vertex.neighbor:
				name = n.getvertex()
				# in node not in new graph, add it
				if name not in g.items.keys():
					g.add(name)
				v = g.getvertex(name)
				v.addneighbor(k,n.getedge())
		return g
	def __repr__(self):
		s=""
		keys = self.items.keys()
		for k in keys:
			# get diction's data element
			v = self.items[k]
			s += str(v) 
		return s
#
# uinit test
# test case: initial test vertex graph and add vertex
# show graph
#

g = vGraph()

g.add("OUTPUT_0")
v = g.getvertex("OUTPUT_0")
v.addneighbor("N9","L13")

g.add("OUTPUT_1")
v = g.getvertex("OUTPUT_1")
v.addneighbor("N8","L14")

g.add("N9")
v = g.getvertex("N9")
v.addneighbor("N6","L11")

g.add("N8")
v = g.getvertex("N8")
v.addneighbor("N7","L10")
v.addneighbor("N4","L7")

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

print(g)
#print("Do DFS search path from OUTPUT_0")
#g.dfs("OUTPUT_0")
#g.dfs("OUTPUT_1")

ig = g.invert()
print(ig)

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
	if re.search("^OUTPUT_[0-9]",k) or \
		re.search("^INPUT_[0-9]",k):
		# do DFS
		g.dfs(k)
		show_trace(g.gettrace())
		g.cleartrace()
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


