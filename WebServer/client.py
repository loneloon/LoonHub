import socket
from _thread import *
import select


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.147.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.state = self.connect()
        self.chat_feed = ''

        self.client.setblocking(False)

    def getState(self):
        return self.state

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(1024).decode()
        except socket.error as e:
            # print(e)
            pass

    def send(self, data=None):
        if data is None:
            data = ''
        try:
            self.client.send(str.encode(data))
            return self.client.recv(1024).decode()
        except socket.error as e:
            # print(e)
            pass

    def read(self):
        self.client.setblocking(True)

        ready = select.select([self.client], [], [], 0.01)
        if ready[0]:
            self.chat_feed = self.client.recv(1024).decode()

        self.client.setblocking(False)


