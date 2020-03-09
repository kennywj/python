#!/usr/bin/python
#
# trans.py, translate netlist to suitable format
# Usage: python trans.py <input nexlist file> [output result file (option)]
#

from __future__ import print_function
import re
import sys
#
# trans.py
#
#	convert ncl netlist file into internal presentation format for further process.
#	Usage:
#		$python3 trans.py <ncl netlist file> < output file>
#

#Data line number used for calculation processing
ln=0

#
# do_drlatr function parsing string pattern
# drlatr  shift2_reg_reg_0__0_U_0 (.rsb ( bufnet_0 ) , .ackout ( n1_N ) , .ackin ( n2_N ) , .f_d ( f_q1_N ) , .t_d ( t_q1_N ) , .f_q ( f_q2_N ) , .t_q ( t_q2_N ));
#
def do_drlatr(k, v, ln):
	l = v.split(' ',2)[-1]
	l = l.replace('(', '').replace(')', '').split(',')
	s1=[]
	s2=[]
	for i in l:
		i = i.strip().split(' ',1)
		if (i[0].strip() == '.f_q' or i[0].strip() == '.t_q'):
			s1.append(i[-1].strip())
		else:
			if (i[0].strip() == '.f_d' or i[0].strip() == '.t_d'):
				s2.append(i[-1].strip())
	outstr = '(' +','.join(map(str,s1)) + ')=' + k.upper() +'_'+ str(ln) + '(' +','.join(map(str, s2)) + ')' + '\n'
	return outstr

#
# do_th function parsing string pattern
# th24comp  U71_U_0_U_0 (.y ( f_n1_N_0 ) , .d ( f_n56 ) , .c ( t_n55 ) , .b ( f_n55 ) , .a ( t_n56 ));
#
def do_th(k, v, ln):
	l = v.split(' ',2)[-1]
	l = l.replace('(', '').replace(')', '').split(',')
	s1 = []
	for i in l:
		i = i.strip().split(' ',1)
		if (i[0].strip() != '.y'):
			s1.append(i[-1].strip())
		else:
			out = i[-1].strip()
	outstr = out + '=' + k.upper()+'_'+ str(ln) + '(' +','.join(map(str, s1)) + ')' + '\n'
	return outstr

#
# do_io function parsing string pattern
# output [7:0] f_mac_out ;
# input ackin ;
#
def do_io(k, v, ln):
	index=0
	r = v.split(' ',1)[0]
	l = v.split(' ',1)[-1]
	outstr=""
	if l == r:
		outstr = k.upper()+'_'+str(ln) + '_' + str(index) + '(' + r + ')' + '\n'
	else:
		r = r.replace('[', '').replace(']', '').split(':')
		end = max(int(r[0]),int(r[1]))
		start = min(int(r[0]),int(r[1]))
		for i in range(end, start-1, -1):
			outstr += k.upper()+'_'+str(ln)+ '_' + str(index) + '(' + l + '[' + str(i) + '])' +'\n'
			index += 1
	return outstr

def parse(line, ln):
	outstr=""
	line = line.replace('\n', '').replace(';', '') 	# remove semicolon and newline
	l = line.strip(' ');							# remove leading/end spaces
	key = l.split(' ',1)[0]
	value = l.split(' ',1)[-1]
	if key == 'input' or key == 'output':
		outstr += do_io(key, value, ln);
	elif re.search('^th[a-z,0-9]', key) or \
		re.search('^and[0-9]', key) or \
		re.search('^inv[0-9]*', key) or \
		re.search('^logic_[0-9]', key):
		outstr += do_th(key,value,ln)
	elif re.search('drlat(r|n)',key):
		outstr += do_drlatr(key, value, ln)
	elif key == "wire" or \
		key == "assign" or	\
		key == "module" or	\
		key == "endmodule" or	\
		re.search('\/\/',key):
		pass
	else:
		print("Line " + str(ln) + " not handle:\"" + line + "\"\n")
	return outstr

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
		ifd = open(sys.argv[1], "r")
	except IOError:
		print ("Could not open read file \"", sys.argv[1],"\"")
		sys.exit()

	# try to open write file
	try:
		ofd = open(sys.argv[2], "w+")
	except:
		pass

	# repeat read line from file
	for line in ifd:
		global ln
		ln+=1
		data = parse(line, ln)
		# try to write data into file
		try:
			ofd.write(data)
		except:
			print(data, end='')
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
