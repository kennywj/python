from __future__ import print_function
import vertex
import stack
import re

#
# vGraph class is vertex name(key) and vertex class (data) pair dictionary
#	 k is vertex, d is a list of nodes which is (vertex, [edge list]) pair
# 		for example:  [v0] - e1 - [v1] (v0 connect to V1 via edge e1)
#					    [v0] - e2 - [v1] (v0 connect to v1 via edge e2) 
#					    [v1] - e3 - [v2] (v1 connect to v2 via edge e3)
#					    [v2] - e4 - [v3] (v2 connect to v3 via edge e4)
#		then then vertex graph should as below
#		vertex_graph = {
#			v0 : [[v1,[e1]], [v2,[e2]]
#			v1 : [[v2,[e3]]
#			v2 : [[v3,[e4]]
#		}
#
def show(g, l):
	for i in l:
		v = g.getvertex(i)
		print(v.getname() + "(" +v.getcolor()+") ", end="")
	print("\n")	
	return
	
class vGraph:
	# graph is a dictionary, key is in/out edge, data is vertex, color and out/in edge
	def __init__(self):
		self.items={}
		self.path=stack.Stack()
		self.trace=[]
		self.count=0
		return

	def add(self, k):
		# if node in vgraph database?
		if self.items.get(k):
			#print("Vertex " + k + "exist")
			return
		else:
			# creat new node
			self.items[k] = vertex.Vertex()
		# set vertex node
		v = self.items[k]
		v.setname(k)
		#print("Add vertex " + k)
		return

	def getkeys(self):
		return self.items.keys()

	def getvertex(self, k):
		return self.items[k]

	def dfs(self, k, func, arg):
		# BFS search vertex in graph
		if not self.items.get(k):
			#print("Vertex " + k + " not exist!")
			return
		# get vertex
		v = self.items[k]
		# puth this vertex
		self.path.push(k)
		#get neighbor list
		n = v.getneighbor()
		if not n:
			# neighbor is null, show path
			# get path lists
			l = self.path.get().copy()
			#self.trace.append(l)
			self.count += 1
			if func!=None:
				func(arg, l)
			else:
				show(None, l)
			#print(self.path)
		else:
			#for each neighbor in neighbor list, do DFS
			for i in n:
				self.dfs(i.getvertex(), func, arg)
		self.path.pop()
		return

	def bfs(self, k, func, arg):
		# BFS search vertex in graph
		if not self.items.get(k):
			#print("Vertex " + k + " not exist!")
			return
		# get vertex
		color=["W","G"]
		qu = []
		visited = []
		self.trace.clear()
		id = 0		# index of color 0/1
		vertex = self.items[k]
		visited.append(vertex)
		vertex.setcolor(color[id])		
		qu.append(vertex.getname())
		while(qu):
			# get first vertex
			vname = qu.pop(0)
			self.trace.append(vname)
			# get data in dictionary by vertex name
			vertex = self.items[vname]
			# get neighbor list
			n = vertex.getneighbor()
			id = (id + 1)%2
			if not n:
				# it is end vertex if without neighbor
				show(self, self.trace)
				self.trace.clear()
				#pass
			else:
				# sequencial put neighbor which does not visited into queue
				for i in n:
					vname = i.getvertex()
					v = self.items[vname]
					if vname not in visited:
						qu.append(vname)
						if not v.getcolor():
							v.setcolor(color[id])
						elif v.getcolor()==color[id]:
							pass
						else:
							print("warning: set " + color[id] +" to " + vname + " but its color was set "+ v.getcolor() )
						visited.append(vname)
					
		return

	def invert(self):
		# invert direction grapy INPUT to OUTPUT /OUTPUT to INPUT
		# create a new graph
		g = vGraph()
		keys = self.items.keys()
		for k in keys:
			vertex = self.items[k]
			name = vertex.getname()
			if name not in g.items.keys():
				g.add(name)
			n = vertex.neighbor
			for i in n:
				name = i.getvertex()
				# in node not in new graph, add it
				if name not in g.items.keys():
					g.add(name)
				v = g.getvertex(name)
				for e in i.getedge():
					v.addneighbor(k,e)
		return g

	def gettrace(self):
		return self.trace

	def cleartrace(self):
		self.trace.clear()
		return
		
	def clear(self):
		self.count = 0
		self.trace.clear()
		self.path.clear()
		return
		
	def __repr__(self):
		s=""
		keys = self.items.keys()
		for k in keys:
			# get diction's data element
			v = self.items[k]
			s += str(v)+"\n"
		return s
		
	def show(self, fd):
		keys = self.items.keys()
		for k in keys:
			# get diction's data element
			self.items[k].show(fd)
		return