#
# unit test
# Test cases create a list of neighbor vertex , then display it by its method
#
import sys
sys.path.append('../')
import neighbor

n = neighbor.Neighbor()
n.setnb("node","edge0")
n.setnb("node","edge1")
n.setnb("node","edge2")

print(n)

print("vertex's name " + n.getname())

print(n.issame("node"))
print(n.issame("node1"))
print(n.issame("1"))
	
l = []
i = 0
while i<10:
	n = neighbor.Neighbor()
	n.setnb("node" + str(i),"edge1"+ str(i))
	i+=1
	l.append(n)
print(l)	

print(l[0].getnb())

l[0].setnb("test","etest")

print(l[0].getnb())

print(l[0])

