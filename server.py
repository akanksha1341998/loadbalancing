import socket
from threading import * 
class server(Thread):
    def __init__(self,port):
        super(server,self).__init__()
        self.port=port
        self.host="localhost"
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        print("Server Socket successfully created ",self.port)
        s.bind((self.host,self.port))
        s.listen()
        while True:
            conn,addr=s.accept()
            conn.sendall("Hello client".encode()) 