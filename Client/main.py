import socket
import sys

ip = sys.argv[-1]
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, 5000))
time = client_socket.recv(1024).decode()
print(time)
client_socket.close()
