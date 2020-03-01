from __future__ import print_function
import node
import stack
import re

'''
def show(n, l):
	print("["+ str(n) +"] ",end='')
	for i in l:
		print(i+"<-",end='')
	print('\n')
	return
'''
def show(n, l):
	print(l)
	return
	
class eGraph:
	# graph is a dictionary, key is in/out edge, data is vetex, color and out/in edge
	def __init__(self):
		self.items={}
		self.path=stack.Stack()
		self.trace=[]
		self.count=0
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
		# BFS search vertex in graph
		if not self.items.get(k):
			print("node " + k + " not exist!")
			return
		queue = []
		visited = []
		
		visited.append(k)
		n = self.items[k]
		self.path.push(k)
		self.path.push('('+n.vertex+')')
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
						self.path.push(e)
						self.path.push('('+self.items[e].vertex+')')
						queue.append(e)
		l = self.path.get().copy()
		self.trace.append(l)
		return

	def dfs(self, k, func, arg):
		if not self.items.get(k):
			print("node " + k + " not exist!")
			return
		n = self.items[k]
		e = n.getedge()
		# push edge into stack
		self.path.push(k)
		# push vertex into stack
		self.path.push(n.vertex)
		# vertex is NULL, end of trace
		if len(e)==1 and \
			(re.search("^INPUT",e[0]) or \
			re.search("^OUTPUT",e[0])):
			# get path lists
			l = self.path.get().copy()
			#self.trace.append(l)
			self.count += 1
			if func!=None:
				func(arg, l)
			else:
				show(None, l)
		else:
			# for each edge in list, do deep seach
			for i in e:
				self.dfs(i, func, arg)
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
	
	def getcount(self):
		return self.count
		
	def clear(self):
		self.count = 0
		self.trace.clear()
		self.path.clear()
		return
		
	def invert(self):
		# create a new graph
		ig = eGraph()
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




