from __future__ import print_function
import neighbor

#
# Vertex class
#    vertex class is a group of vertex and its neighbors 
#	 the neighbor is a element of neighbor class
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
		# verify if this node & edges already in list?
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
			s += "   +--"+ i.getedge() + "->[" + i.getvertex() +"]\n"
		s+="\n"
		return s
