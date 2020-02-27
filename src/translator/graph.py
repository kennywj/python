from __future__ import print_function
import node
import stack
import re

def show(n, l):
	print("["+ str(n) +"] path: ",end='')
	for i in l:
		print(i+"<-",end='')
	print('\n')
	return

class Graph:
	# graph is a dictionary, key is in/out edge, data is vetex, color and out/in edge
	def __init__(self):
		self.items={}
		self.path=stack.Stack()
		self.trace=[]
		return

	def add(self, k, e):
		if not self.items.get(k):
			# creat new node
			self.items[k] = node.Node()
		# get node
		n = self.items[k]
		# first element if list is vertex, other are edges
		n.setvertex(e[0])
		for i in range(1,len(e)):
			n.addedge(e[i])
		self.items[k] = n
		return

	def getkeys(self):
		return self.items.keys()

	def getvertex(self, k):
		return self.items[k].getvertex()

	def bfs(self,k):
		# Create a queue for BFS, a queued for visited edge and node
		queue = []
		visited = []

		visited.append(k)
		n = self.items[k]
		#visited.append(n.getvertex())
		queue.append(k)
		while(queue):
			k = queue.pop()
			n = self.items[k]
			for e in n.getedge():
				if not(re.search("^INPUT",e) or \
					re.search("^OUTPUT",e)):
					if e not in visited:
						visited.append(e)
						i = self.items[e]
						#visited.append(i.getvertex())
						queue.append(e)
		print(visited)
		return

	def dfs(self, k):
		n = self.items[k]
		e = n.getedge()
		# push edge into stack
		self.path.push(k)
		# push vertex into stack
		self.path.push('['+n.vertex+']')
		# vertex is NULL, end of trace
		if len(e)==1 and \
			(re.search("^INPUT",e[0]) or \
			re.search("^OUTPUT",e[0])):
			# get path lists
			l = self.path.get().copy()
			self.trace.append(l)
			#show(len(self.trace), l)
		else:
			# for each edge in list, do deep seach
			for i in e:
				self.dfs(i)
		#pop vertex from stack
		self.path.pop()
		#pop edge from stack
		self.path.pop()
		return

	def gettrace(self):
		return self.trace

	def cleartrace(self):
		self.trace.clear()
		return

	def invert(self):
		# create a new graph
		ig = Graph()
		keys = self.items.keys()
		for k in keys:
			# get node in graph dictionary
			n = self.items[k]
			v = n.getvertex()
			c = n.getcolor()
			for e in n.getedge():
				# check if key (e) exist?
				if not ig.items.get(e):
					# creat new node
					ig.items[e] = node.Node()
					x = ig.items[e]
					x.setvertex(v)
					x.setcolor(c)
				else:
					x = ig.items[e]
				if k not in x.getedge():
					x.addedge(k)
		return ig

	def __repr__(self):
		s =""
		keys = self.items.keys()
		for k in keys:
			# get diction's data element
			n = self.items[k]
			s += "key ="+ k + ", vertex= " + n.getvertex() + \
				" color " + str(n.getcolor()) + " edge = ["
			e = n.getedge()
			while (e):
				s += e.pop(0)
				if len(e)>0:
					s += ','
			s += "]\n"
		return s

	def show(self):
		return print(self)

#
# uinit test
# test case: initial test graph and show graph
# give virtual line OUTPUT_[0-9], INPUT_[0-9]
#
'''
g = Graph()
g.add("OUTPUT_0",["OUTPUT","L13"])
g.add("OUTPUT_1",["OUTPUT","L14"])
g.add("L13",["N9","L11"])
g.add("L14",["N8","L7","L10"])
g.add("L11",["N6","L1","L6"])
g.add("L10",["N7","L8","L9"])
g.add("L8",["N4","L2","L3"])
g.add("L9",["N5","L4","L5"])
g.add("L7",["N4","L2","L3"])
g.add("L6",["N4","L2","L3"])
g.add("L5",["INUPT","INPUT_4"])
g.add("L4",["INUPT","INPUT_3"])
g.add("L3",["INUPT","INPUT_2"])
g.add("L2",["INUPT","INPUT_1"])
g.add("L1",["INUPT","INPUT_0"])

print("Original Graph")
#print(g)
g.show()
#repr(g)
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


