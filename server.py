import socket
import os 
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
            data=conn.recv(1024)
            fname=data.decode()
            
            if os.path.isfile("TextFILES/"+fname):
                conn.send("File exist".encode())
                f=open("TextFILES/"+fname,"rb")
                content=f.read()
                conn.send(content)
                f.close()
            else:
                conn.send ("File not exist".encode())
            
            
             
            