from __future__ import print_function
import vertex
import stack
import re

#
# vGraph class is vertex name(key) and vertex class (data) pair dictionary
#
#
class vGraph:
	# graph is a dictionary, key is in/out edge, data is vetex, color and out/in edge
	def __init__(self):
		self.items={}
		self.path=stack.Stack()
		self.trace=[]
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

	def dfs(self,k):
		# BFS search vertex in graph
		if not self.items.get(k):
			print("Vertex " + k + " not exist!")
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
			self.trace.append(l)
			#print(self.path)
		else:
			#for each neighbor in neighbor list, do DFS
			for i in n:
				self.dfs(i.getvertex())
		self.path.pop()
		return

	def bfs(self, k):
		# BFS search vertex in graph
		if not self.items.get(k):
			print("Vertex " + k + " not exist!")
			return
		# get vertex
		queue = []
		visited = []
		self.trace.clear()
		
		vertex = self.items[k]
		visited.append(vertex)
		queue.append(vertex.getname())
		while(queue):
			# get first vertex
			vname = queue.pop(0)
			self.trace.append(vname)
			# get data in dictionary by vertex name
			vertex = self.items[vname]
			# get neighbor list
			n = vertex.getneighbor()
			if not n:
				# it is end vertex if without neighbor
				pass
			else:
				# sequencial put neighbor which does not visited into queue
				for i in n:
					vname = i.getvertex()
					v = self.items[vname]
					if vname not in visited:
						queue.append(vname)
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
				v.addneighbor(k,i.getedge())
		return g

	def gettrace(self):
		return self.trace

	def cleartrace(self):
		self.trace.clear()
		return

	def __repr__(self):
		s=""
		keys = self.items.keys()
		for k in keys:
			# get diction's data element
			v = self.items[k]
			s += str(v)
		return s
