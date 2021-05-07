import socket

clientx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientx.connect(("127.0.0.1",1024))

while True:
    data = input("Message: ")

    clientx.send((data).encode())

    receive = clientx.recv(1024)

    print(receive)
