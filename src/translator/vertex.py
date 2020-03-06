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
		self.color= ""
		self.neighbor=[]
		return

	def setname(self, v):
		self.name = v
		return

	def getname(self):
		return self.name

	def addneighbor(self, v, e):
		# verify if this node already in list? only put egde in vertex
		for n in self.neighbor:
			if n.issame(v):
				n.setedge(e)
				return
		# add the new neighbor
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
		s = self.name + " : "
		if not self.neighbor:
			s += "(None)"
		else:
			for i in self.neighbor:
				s += str(i)+ ","
		return s+"\n"

	def show(self, fd):
		s = "[" + self.name + "], color=" + self.color +"\n"
		for i in self.neighbor:
			s1 = "  => [" + i.getvertex() +"]\n"
			s2 = ""
			n=0
			for e in i.getedge():
				# print list use '", ".join(e)'
				s2 += "        path " + str(n) +":\"" + str(e) + "\"\n"
				n+=1
			s += s1 + s2
		s+="\n"
		
		if fd:
			fd.write(s)
		else:
			print(s)
		return
