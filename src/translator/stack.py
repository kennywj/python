from __future__ import print_function

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)
 
	def get(self):
		return self.items
	
	def __repr__(self):
		s=""
		for i in self.items:
			s += str(i) + ","
		return s
		
# unit test
# Test cases create a new node, then display it
#
'''
s = Stack()

s.push(1)
s.push(2)
s.push(3)
print(s)
print(s.isEmpty())

print(s.peek())
n = s.pop()
print (str(n))
print(s.peek())

print(s.size())

s.pop()
s.pop()
s.push(4)
print(s.isEmpty())
s.pop()
print(s.isEmpty())
'''
