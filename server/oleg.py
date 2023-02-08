import socket
from datetime import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('10.171.132.172', 5000))
server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Accepted connection from {client_address}')
    client_socket.send(("Alexandr Belofastov server time: " + str(datetime.now())).encode())
    client_socket.close()