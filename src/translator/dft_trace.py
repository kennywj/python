#
# dft_trace, generate edge graph, then remove none latch nodes and translate to vertex graph
# then do DFS search from OUTPUT to INPUT to list all latch nodes
#
import time
from datetime import timedelta
import sys
sys.path.append('../')
import egraph
import vgraph
from gengraph import gen_egraph
from gengraph import process
import timer

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
		
		
def show_progress(g, start_time):
	count = g.getcount()
	elapsed_time = time.time() - start_time
	print(str(timedelta(seconds=int(elapsed_time))),end="")
	print(" process number = " + str(count),end="\r")
	return

	
def main():
	# try to open read file
	if len(sys.argv) <= 1:
		print ("dft_trace.py <inputfile> [<outputfile>]")
		sys.exit()
	g = gen_egraph(sys.argv[1])
	if not g:
		print("cannot create graph, exit")
		sys.exit()
	else:
		g.clear()
	
	start_time = time.time()
	t = timer.RepeatTimer(1, show_progress, [g, start_time])
	# start timer
	t.start()
	vg = vgraph.vGraph()
	# DFS OUTPUT_0 path, put in vg
	g.dfs("OUTPUT_0",process, vg)
	
	print(vg)
	# stop timer
	t.cancel()
	'''
	# try to open write file
	try:
		ofd = open(sys.argv[2], "w+")
	except:
		pass
		
	print(g)
	# trace 1 OUTPUT line for test
	g.dfs("OUTPUT_0", None)
	# try to write data into file
	try:
		write_trace(ofd, l)
	except:
		pass
		
	g.cleartrace()
	
	try:
		ofd.close()
	except:
		pass
	'''
#
# end main progam
#
if __name__ == '__main__':
	main()