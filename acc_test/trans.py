#!/usr/bin/python
#
# trans.py, extrace data from c statement
# Usage: python3 trans.py <input text file> [output binary data (option)]
#

from __future__ import print_function
import re
import sys
from utility import * 

def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurrences streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurrence single-line comments (//COMMENT\n ) from string
    return string	
	
def parse(line, ln):
	line = removeComments(line)
	if not line.strip():
		print("line "+str(ln)+": empty, ignore")
		return None
	line = line.replace('\n', '').replace(';', '') 	# remove semicolon and newline
	l = line.strip(' ');							# remove leading/end spaces
	l = l.replace('(', '').replace(')', '').split(',')
	l = l[-1].strip(' ');
	if l=='':
		return None
	return l

#
# start main program
#
def main():
	data = ""
	# try to open read file
	if len(sys.argv) <= 1:
		print ("trans.py <inputfile> [<outputfile>]")
		sys.exit()
	try:
		ifd = open(sys.argv[1], 'r')
	except IOError:
		print ("Could not open read file \"", sys.argv[1],"\"")
		sys.exit()
		
	big = query_yes_no("generate big endian data:","no")
	# try to open write file
	try:
		ofd = open(sys.argv[2], 'wb')
	except:
		pass
	ln = 0
	# repeat read line from file
	for line in ifd:
		ln += 1
		data = parse(line, ln)
		if not data:
			continue
		v = int(str(data[2:]),16)
		# try to write data into file
		try:
			if big==True:
				ofd.write(v.to_bytes(4, "big"))
			else:
				ofd.write(v.to_bytes(4, "little"))
		except:
			print(str(ln)+" " + data)
	# close read file
	ifd.close()

	# try to close write file
	try:
		ofd.close
	except:
		pass
	print("Translation format processing Done.")
#
# end main progam
#
if __name__ == '__main__':
	main()
