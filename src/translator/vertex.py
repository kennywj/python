from __future__ import print_function
import neighbor

#
# Vertex graph class
#    vertex graph {k:d} is s direction graph, 
#	 k is vertex, d is a list of node which node is (vertex, edge) pair
# 		for example: [v0] - e1 - [v1] (v0 connect to V1 via edge e1)
#					 [v0] - e2 - [v2] (v0 connect to v2 via edge e2) 
#					 [v1] - e3 - [v2] (v1 connect to v2 via edge e3)
#					 [v2] - e4 - [v3] (v2 connect to v3 via edge e4)
#		then then vertex graph should as below
#		vertex_graph = {
#			v0 : [[v1,e1], [v2,e2]]
#			v1 : [[v2,e3]]
#			v2 : [[v3,e4]]
#		}
#
class Vertex:
	def __init__(self):
		self.name = ""
		self.color=0
		self.neighbor=[]
		return

	def setname(self, v):
		self.name = v
		return

	def getname(self):
		return self.name
		
	def addneighbor(self, v, e):
		# verify if this not already in list?
		for n in self.neighbor:
			if n.issame(v,e):
				#print("Vertex " + v +", edge " + e + " exist");
				return
		# add the new neighbor
		#print("add neighbor" + v +"," + e)
		n = neighbor.Neighbor()
		n.setnb(v, e)
		self.neighbor.append(n)
		return
	
	def delneighbor(self, v):
		for n in self.neighbor:
			if n.getvertex()==v:
				self.neighbor.pop(self.neighbor.index(n))
		return
	
	def getneighbor(self):
		return self.neighbor
		
	def isneighbor(self, v):
		for n in self.neighbor:
			if n.getvertex() == v:
				return True
		return False
		
	def setcolor(self, c):
		self.color = c
	
	def getcolor(self):
		return self.color
		
	def __repr__(self):
		s = "[" + self.name + "], color = " + str(self.color) + "\n"
		for i in self.neighbor:
			s += "   neighbor --"+ i.getedge() + "->[" + i.getvertex() +"]\n"
		s+="\n"
		return s
