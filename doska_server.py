import socket
from time import sleep


class callboard():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @property
    def get_news(self):
        f = open('news.txt', 'r')
        message = []
        for i in f:
            message.append(i)
            sleep(1)
        f.close()
        return "".join(message)

    def conn(self):
        sock = socket.socket()
        sock.bind((self.ip, self.port))
        sock.listen(1)
        print('waiting for connection...')
        conn, addr = sock.accept()
        print('connected', addr)
        data = conn.recv(1024)
        uData = data.decode('utf-8')
        if uData == "LIST":
            message = self.get_news
            print('Client -> {}'.format(message))
            conn.send(message.encode('utf-8'))
        else:
            f = open('news.txt', 'a')
            f.write(uData+";\n")
            conn.send("Message successfully added".encode('utf-8'))
        conn.close()


server = callboard('', 9090)
server.conn()
