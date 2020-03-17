#
# gen_vgraph, generate edge graph, then remove none latch nodes and translate to vertex graph
# then do DFS search from OUTPUT to INPUT to list all latch nodes
#
# -*- coding: utf-8 -*-
import re
import os
import sys
sys.path.append('../')
import time
from datetime import timedelta
from multiprocessing import Process, JoinableQueue
import timer
# private module
import egraph
import vgraph
from gengraph import gen_egraph
from gengraph import process


#
# egraph2vgraph.py
#
#	To convert edge graph file into vertex graph object (python dictionary) and then write to file.
#  The edge graph file from NCL netlist file converted by trans.py 
#
#	Usage:
#		$python3 egraph2vgraph.py <vgraph file>
#
def show_progress(start_time):
	elapsed_time = time.time() - start_time
	print("process time: "+str(timedelta(seconds=int(elapsed_time))))
	return

def handler(qu):
	print("Start vertex graph process")
	vg = vgraph.vGraph()
	count = 0
	max_size = 0
	while True:
		total = qu.qsize()
		if total > max_size:
			max_size = total
		l = qu.get()
		if l==None:
			qu.put(vg)
			print("put vertex graph into queue, then exit")
			break;
		count +=1
		if (count & 0xFFF)==0:
			print("{:.2%}".format(count / max_size), end = "\r")
		#print("Pid["+str(os.getpid())+"] waiting process: "+str(qu.qsize())+" vertex number =" + str(len(vg)),end="\r")
		process(vg, l)
		qu.task_done()
	print("end vertex graph process")
	return


def do_process(qu, l):
	# send path list to queue
	#print(str(os.getpid())+":"+str(qu.qsize()),end="\r")
	qu.put(l)
	return
	
def do_dfs(g, k, qu):
	print("\nPid["+ str(os.getpid())+"] DFS search start from " + k)
	g.dfs(k, do_process, qu)
	print("\nPid[" + str(os.getpid())+ "] " + k +" " + str(g.getcount()) + " Done ")
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
	
	# 建立 IPC Queue
	qu = JoinableQueue()
	# create empty vertex queue
	vg = vgraph.vGraph()
	
	# 建立 handler process
	hd = Process(target=handler, args=(qu,))
	hd.start()
	
	start_time = time.time()
	#t = timer.RepeatTimer(0.5, show_progress, [g, start_time])
	# start timer
	#t.start()
	
	# 建立process list
	plist=[]
	# Do DFS of edge graph to generate Vertex graph
	keys = g.getkeys()
	for k in keys:
		if re.search("^OUTPUT_",k):
			p = Process(target=do_dfs, args=(g, k, qu, ))
			p.start()
			plist.append(p)
			
	# 等待所有 child processes 完成
	for p in plist:
		p.join()
	print("\nAll DFS process done\n")	
	# stop timer
	#t.cancel()
	
	# inform process to exit
	qu.put(None)
	g = qu.get()
	qu.task_done()
	# wait HD process exit
	hd.join()
	#print("\nExit HD process\n")
	# display invert vertex graph
	if g:
		g.show(None)
	show_progress(start_time)
	
#
# end main progam
#
if __name__ == '__main__':
	main()
