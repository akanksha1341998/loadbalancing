import socket
from threading import *
class loadbalancer(Thread):
    def __init__(self,conn,addport,addr):
        super(loadbalancer,self).__init__()
        self.port=addport
        print("Client ",addr)
        print("connected to server on port ",addport)
        self.conn=conn
    def run(self):
        data=self.conn.recv(1024)
        fname=data.decode()+".txt"
        self.so=socket.socket()
        self.so.connect(("localhost",self.port))
        self.so.send(fname.encode())
        data=self.so.recv(1024)
        self.conn.send(data)
        if data.decode()=="File exist":
            content=self.so.recv(1024)
            self.conn.send(content)
        self.so.close()
        #self.conn.send(data)
        
        