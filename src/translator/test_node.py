import node
# unit test
# Test cases create a new node, then display it
#

n = node.Node()
n.setvertex("III")
n.setcolor(1)
n.addedge("line0")
n.addedge("line0")
n.addedge("line1")
n.addedge("line2")
e = n.getedge()
for i in e:
	print(i)
print(n)
n.deledge("line2")
n.deledge("line3")
n.setcolor(2)
print(n)
