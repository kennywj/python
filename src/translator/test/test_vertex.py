import sys
sys.path.append('../')
import vertex
#
# unit test
# Test cases create a new vertex, test methods of vertex
#

v = vertex.Vertex()

v.setname("INPUT_0")
v.setcolor(1)
v.addneighbor("N1","e1")
v.addneighbor("N1","e10")
v.addneighbor("N1","e11")
v.addneighbor("N2","e2")
v.addneighbor("N3","e3")
v.addneighbor("N4","e4")
v.addneighbor("N4","e4")
v.addneighbor("N3","e3")
v.addneighbor("N3","e13")
print(v)

v.show(None)

print("Is N1 neighbor? " + str(v.isneighbor("N1")))
v.delneighbor("N1")
print(v)
print("Is N1 neighbor? " + str(v.isneighbor("N1")))

v.delneighbor("N1")
v.delneighbor("N3")
print(v)
