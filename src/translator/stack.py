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
		
