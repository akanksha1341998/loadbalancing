import socket
from threading import *
class loadbalancer(Thread):
    def __init__(self,conn,addport):
        super(loadbalancer,self).__init__()
        self.port=addport
        print("Client connected to ",addport)
        self.conn=conn
    def run(self):
        data=self.conn.recv(1024)
        print(data.decode())
        self.so=socket.socket()
        self.so.connect(("localhost",self.port))
        data=self.so.recv(1024)
        print(data.decode())
        self.conn.send(data)
        
        