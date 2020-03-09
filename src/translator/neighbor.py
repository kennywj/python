from __future__ import print_function

#
# Neighbor define the vertex and edge connected from key vertex in Vgraph
# [key node(vertex]-Neighbor.edge-[Neighbor.vertex]
#
class Neighbor:
	def __init__(self):
		self.vertex =""
		self.edge = [] # edge is a list of strings
		return

	def setnb(self, v, e):
		self.vertex = v
		self.edge.append(e)
		return

	def getnb(self):
		# get neighbor node (vertex and edges)
		n=[]
		n.append(self.vertex)
		n.append(self.edge)
		return n

	def getname(self):
		return self.vertex

	def setedge(self, e):
		if e not in self.edge:
			self.edge.append(e)

	def getedge(self):
		return self.edge

	def issame(self, v):
		return self.vertex == v

	def __repr__(self):
		return self.vertex

	def show(self):
		s = "(" + self.vertex + ":" + ", ".join(self.edge) + ")"
		return s

