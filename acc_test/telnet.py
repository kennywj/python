#
# S7 FPGA verify program
#
import telnetlib
import time
#HOST = input("Enter host IP: ")

tn = telnetlib.Telnet("localhost", port=4444, timeout=10)

if tn:
    #tn.set_debuglevel(2)
    #tn.write(telnetlib.IAC+telnetlib.DONT+telnetlib.ECHO) 
    tn.interact()