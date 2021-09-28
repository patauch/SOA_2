import socket

class word_sort():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def sort(self, data):
        word_split = data.split()
        word_split = list(set(word_split))
        for i in range(0, len(word_split)):
            word_split[i] = ''.join(e for e in word_split[i].lower() if e.isalnum())
        word_split = sorted(word_split)
        word_split = list(set(word_split))
        word_split = "\n".join(word_split)
        return word_split

    def conn(self):
        sock = socket.socket()
        sock.bind((self.ip, self.port))
        sock.listen(1)
        print('waiting for connection...')
        conn, addr = sock.accept()
        print('connected', addr)
        data = conn.recv(1024)
        uData = self.sort(data.decode('utf-8'))
        print('Client -> {}'.format(uData))
        conn.send(uData.encode('utf-8'))
        conn.close()


server = word_sort('', 9090)
server.conn()

