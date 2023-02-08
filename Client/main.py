import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.171.132.172', 5000))
time = client_socket.recv(1024).decode()
print(time)
client_socket.close()