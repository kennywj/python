# -*- coding: utf-8 -*-
import time
from datetime import timedelta
import sys
sys.path.append('../')
import timer

count =0

def time_handler(arg, start_time):
	global count
	print(arg+" ")
	elapsed_time = time.time() - start_time
	print(str(timedelta(seconds=int(elapsed_time))),end="")
	#print("Elapsed time : %.3f" % elapsed_time,end="")
	print(" count = " + str(count))
	count+=1
	return

start_time = time.time()
t = timer.RepeatTimer(1, time_handler, ["test", start_time])
t.start()

time.sleep(30)

t.cancel()
