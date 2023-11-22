import socket
import struct

created_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
created_socket.connect(('127.0.0.1', 2998))
received_data = created_socket.recv(4)

received_number = struct.unpack("I", received_data)[0]
received_string = str(received_number)
received_string_bytes = received_string.encode()

created_socket.sendall(received_string_bytes)

received_data = created_socket.recv(100)
print(received_data)
created_socket.close()