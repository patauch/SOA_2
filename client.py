import socket
sock = socket.socket()
sock.connect(('localhost', 9090))
message = input("Введите ваше сообщение: ")

sock.send(message.encode("utf-8"))

data = sock.recv(1024)
udata = data.decode('utf-8')
print('server > {}'.format(udata))
sock.close()
