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
		self.group = 0
		self.ib = False
		self.neighbor=[]
		return

	def setname(self, v):
		self.name = v
		return

	def getname(self):
		return self.name

	def addneighbor(self, v, e):
		# verify if this node already in list? if yes, only put its edge in vertex edge list
		for n in self.neighbor:
			if n.issame(v):
				n.setedge(e)
				return
		# add the new neighbor and its edge
		n = neighbor.Neighbor()
		n.setnb(v, e)
		self.neighbor.append(n)
		return

	def delneighbor(self, v):
		for n in self.neighbor:
			if n.getname()==v:
				self.neighbor.pop(self.neighbor.index(n))
		return

	def getneighbor(self):
		return self.neighbor

	def isneighbor(self, v):
		for n in self.neighbor:
			if n.getname() == v:
				return True
		return False

	# set color string
	def setcolor(self, c):
		self.color = c

	def getcolor(self):
		return self.color

	# set group number
	def setgroup(self, n):
		self.group = n

	def getgroup(self):
		return self.group

	# set PO
	def setib(self, b):
		self.ib = b

	def getib(self):
		return self.ib

	def clear(self):
		self.color= ""
		self.group = 0
		self.ib = False
		return
		
	def __repr__(self):
		s = self.name
		if self.ib:
			s += "(IB):"
		else:
			s += "    :"
		if not self.neighbor:
			s += "(None)"
		else:
			for i in self.neighbor:
				s += str(i)+ ","
		return s+"\n"

	def show(self, fd):
		s = "[" + self.name + "], color= " + str(self.color) + ",group= "+ str(self.group)
		if self.ib:
			s += " IB\n"
		else:
			s +="\n"
		for i in self.neighbor:
			s1 = "  => [" + i.getname() +"]\n"
			s2 = ""
			n=0
			for e in i.getedge():
				# print list use '", ".join(e)'
				s2 += "        path " + str(n) +":\"" + str(e) + "\"\n"
				n+=1
			s += s1 + s2
		if fd:
			fd.write(s)
		else:
			print(s)
		return
