from __future__ import print_function

class Node:
	def __init__(self):
		self.vertex=""
		self.color=0
		self.edge=[]
		return

	def setvertex(self, v):
		self.vertex = v
		return

	def getvertex(self):
		return self.vertex
		
	def addedge(self, e):
		if e not in self.edge:
			self.edge.append(e)
		else:
			print("duplicate edge: " + e)
		return
	
	def deledge(self, e):
		if e in self.edge:
			self.edge.remove(e)
		else:
			print("edge: " + e + " not exist")
		return
		
	def getedge(self):
		return self.edge
		
	def setcolor(self, c):
		self.color = c
	
	def getcolor(self):
		return self.color
	
	def show(self):
		print("Vertex = " + self.vertex + ", color = " + str(self.color) +" edge =", end='')
		for i in self.edge:
			print( i + ",", end ="")
		print("");
		return

# unit test
# Test cases create a new node, then display it
#
'''
n = Node()
n.setvertex("III")
n.setcolor(1)
n.addedge("line0")
n.addedge("line0")
n.addedge("line1")
n.addedge("line2")
e = n.getedge()
for i in e:
	print(i)
n.show()
n.deledge("line2")
n.deledge("line3")
n.setcolor(2)
n.show()
'''