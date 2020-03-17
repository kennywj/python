#
# dft_trace, generate edge graph, then remove none latch nodes and translate to vertex graph
# then do DFS search from OUTPUT to INPUT to list all latch nodes
#
import re
import time
from datetime import timedelta
import sys
import egraph
import vgraph
from gengraph import gen_egraph
from gengraph import process
import timer

#
# gen_vgraph.py
#
#	To convert edge graph file into vertex graph object (python dictionary) and then write to file.
#  The edge graph file from NCL netlist file converted by trans.py 
#
#	Usage:
#		$python3 gen_vgraph.py <vgraph file>
#

def show_progress(g, start_time):
	count = g.getcount()
	elapsed_time = time.time() - start_time
	print(str(timedelta(seconds=int(elapsed_time))),end="")
	print(" process number = " + str(count),end="\r")
	return


def main():
	# try to open read file
	if len(sys.argv) <= 1:
		print ("gen_vgraph.py <input file> [output vgraph file] [invert vgraph file]")
		sys.exit()
	# generate edge graph
	g = gen_egraph(sys.argv[1])
	if not g:
		print("cannot create graph, exit")
		sys.exit()
	else:
		g.clear()

	try:
		vgraph_fname = sys.argv[2]
	except:
		print("\nWrite vertex graph into file")
		vgraph_fname = input("input filename:")
	try:
		invert_vgraph_fname = sys.argv[3]
	except:
		print("\nWrite invert vertex into file")
		invert_vgraph_fname = input("input filename:")

	# Do DFS of edge graph to generate Vertex graph
	start_time = time.time()
	t = timer.RepeatTimer(0.5, show_progress, [g, start_time])
	# start timer
	t.start()
	vg = vgraph.vGraph()
	keys = g.getkeys()
	for k in keys:
		if re.search("^OUTPUT_",k):
			print("\nDFS search start from " + k)
			g.dfs(k, process, vg)

	# stop timer
	t.cancel()

	# display invert vertex graph
	try:
		ofd = open(vgraph_fname, "w+")
	except:
		print ("Could not open write file \"" + fname + "\"")
		sys.exit()
	# show vertex graph (write to file)
	vg.show(ofd)
	try:
		ofd.close
	except:
		pass

	# trace invert vertex graph
	try:
		ofd = open(invert_vgraph_fname, "w+")
	except:
		print ("Could not open write file \"" + fname + "\"")
		sys.exit()

	# invert vertex graph
	ivg = vg.invert()
	# show vertex graph (write to file)
	ivg.show(ofd)
	try:
		ofd.close
	except:
		pass

	elapsed_time = time.time() - start_time
	print("\nprocess time: "+str(timedelta(seconds=int(elapsed_time))))
#
# end main progam
#
if __name__ == '__main__':
	main()
