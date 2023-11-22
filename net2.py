import socket
import struct

created_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
created_socket.connect(('127.0.0.1', 2997))

received_numbers_sum = 0
for i in range(4):
    received_data = created_socket.recv(4)
    received_number = struct.unpack('I', received_data)[0]
    received_numbers_sum += received_number

received_numbers_sum_bytes = struct.pack('I', received_numbers_sum)
created_socket.sendall(received_numbers_sum_bytes)

received_data = created_socket.recv(100)
print(received_data)
created_socket.close()