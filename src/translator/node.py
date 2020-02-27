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
	
	def __repr__(self):
		s = "Vertex = " + self.vertex + ", color = " + str(self.color) +" edge ="
		for i in self.edge:
			s += i + ","
		s+="\n";
		return s

