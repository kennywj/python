
import sys
import re
from gengraph import gen_egraph

def show_trace(l):	
	id=0
	for i in l:
		n = l.pop()
		id+=1
		print("Path [" + str(id) +"] :")
		while(len(n)):
			v = n.pop()
			if re.search("^OUTPUT_[0-9]",v) or \
				re.search("^INPUT_[0-9]",v):
				pass
			else:
				print(v,end="")
				if len(n)>1:
					print("->",end="")
		print("\n")
		
def write_trace(ofd, l):	
	id=0
	for i in l:
		n = l.pop()
		id += 1
		ofd.write("Path [" + str(id) +"] :")
		while(len(n)):
			v = n.pop()
			if re.search("^OUTPUT_[0-9]",v) or \
				re.search("^INPUT_[0-9]",v):
				pass
			else:
				ofd.write(v)
				if len(n)>1:
					ofd.write("->")
		ofd.write("\n")
		
def main():
	# try to open read file
	if len(sys.argv) <= 1:
		print ("dft_trace.py <inputfile> [<outputfile>]")
		sys.exit()
	g = gen_egraph(sys.argv[1])
	if not g:
		print("cannot create graph, exit")
		sys.exit()
	
	# try to open write file
	try:
		ofd = open(sys.argv[2], "w+")
	except:
		pass
		
	print(g)
	# trace 1 OUTPUT line for test
	g.dfs("OUTPUT_0")
	l = g.gettrace()
	# try to write data into file
	try:
		write_trace(ofd, l)
	except:
		show_trace(l)
	g.cleartrace()
	try:
		ofd.close()
	except:
		pass
		
	'''	
	keys = g.getkeys()	
	#print(len(keys))

	for k in keys:
	#	if re.search("^INPUT",k) or \
	#		re.search("^OUTPUT",k):
		if re.search("^OUTPUT",k):
			g.dfs(k)
	'''
#
# end main progam
#
if __name__ == '__main__':
	main()