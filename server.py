import socket
from threading import * 
class server(Thread):
    def __init__(self,port,weight):
        super(server,self).__init__()
        self.port=port
        self.host="localhost"
        self.weight=weight
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        print("Server Socket successfully created ",self.port)
        try:
            s.bind((self.host,self.port))
        except socket.error as e:
            print(str(e))
        s.listen()
        while True:
            conn,addr=s.accept()
           
            conn.sendall("Hello client".encode()) 
    