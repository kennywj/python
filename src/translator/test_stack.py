import stack
# unit test
# Test cases create a new node, then display it
#

s = stack.Stack()

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

