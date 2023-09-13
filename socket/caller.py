import socket

HOST = '127.0.0.1'
PORT = 6789

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    with client:
        # Client Connect
        client.connect((HOST, PORT))
        client.sendall(b"Hello, world")
        data = client.recv(1024)
        print(data)
except Exception as e:
    print('Cannot connect: ' + str(e))
        