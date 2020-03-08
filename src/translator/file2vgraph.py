import re
import sys
sys.path.append('../')
import vgraph

def trans_vgraph(fd):
	vg = vgraph.vGraph()
	neighbor=""
	vertex=None
	# repeat read line from file
	while True:
		try:
			line = fd.readline()
		except IOError:
			print ("Could not read file")
			break
		if not line:
			break
		line = line.replace('\n', '').strip(' ')	# remove and newline and remove leading/end spaces
		# find "color=", add vertex
		#print(line)
		if line.find("color=")>=0:
			l = line.replace("[","").replace("]","").split(",")
			vg.add(l[0])
			vertex = vg.getvertex(l[0])
		# find "=>", add neighbor	
		elif line.find("=>")>=0:
			l = line.replace("[","").replace("]","").split(" ")	
			neighbor = l[1]
		elif line.find("path")>=0:
			# get path
			l = line.replace("\"","").split(":")	
			if vertex and neighbor:
				# add path
				vertex.addneighbor(neighbor,l[1])
		else:
			if line != "":
				print("warning: not process " + line)
	return vg

def main():
	# try to open read file
	if len(sys.argv) <= 1:
		print ("file2vgraph.py <inputfile>")
		sys.exit()
	try:
		fd = open(sys.argv[1], "r")
	except IOError:
		print ("Could not open read file \"", sys.argv[1],"\"")
		sys.exit()
	
	vg = trans_vgraph(fd)
	# close read file
	fd.close()
	print("Translation file to Vertex graph Done.")
	
	if not vg:
		sys.exit()
	# mark vertex same group
	vg.bfs("INPUT_",None,None)
	vg.show(None)
	return
#
# end main progam
#
if __name__ == '__main__':
	main()		