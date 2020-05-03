import socket
from loadbalancer import loadbalancer 
from server import server
from threading import *

host="localhost"
port=12345
ad=4000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Main Socket successfully created")
s.bind((host,port))
s.listen()

s1 = server(4001)
s2 = server(4002)
s1.start()
s2.start()
print('socket is listening')
while True:
    conn,addr=s.accept()
    if ad==4002:
            ad=4000
    ad=ad+1
    ld=loadbalancer(conn,ad)
    ld.start()

