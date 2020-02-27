from __future__ import print_function

#
# Neighbor define the vertex and edge connected from key vertex in Vgraph
# [key node(vertex]-Neighbor.edge-[Neighbor.vertex]
#
class Neighbor:
	def __init__(self):
		self.vertex =""
		self.edge = ""
		return

	def setnb(self, v, e):
		self.vertex = v
		self.edge = e 
		return

	def getnb(self):
		n=[]
		n.append(self.vertex)
		n.append(self.edge)
		return n
	
	def getvertex(self):
		return self.vertex
		
	def getedge(self):
		return self.edge
	
	def issame(self, v, e):
		return self.vertex == v and self.edge == e
	
	def __repr__(self):
		return "(" + self.vertex + "," + self.edge + ")"

#
# unit test
# Test cases create a list of neighbor vertex , then display it by its method
#
'''
n = Neighbor()
n.setnb("node","edge")

print(n.issame("node","edge"))

print(n.issame("1","2"))
	
l = []
i = 0
while i<10:
	n = Neighbor()
	n.setnb("node" + str(i),"edge1"+ str(i))
	i+=1
	l.append(n)
print(l)	

print(l[0].getnb())

l[0].setnb("test","etest")

print(l[0].getnb())

print(l[0])
'''
