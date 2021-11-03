import socket
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect(('localhost', 1000))
data = client1.recv(4096)
client1.close()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', int(data.decode())))
while True:
    a=input('0:')
    client.send(a.encode())
    from_server = client.recv(4096)
    print(from_server.decode())
    if from_server.decode() =='stopconnect':
        break
