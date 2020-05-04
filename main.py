import socket
from loadbalancer import loadbalancer 
from server import server
from threading import *
connum=0
host="localhost"
port=12345
ad=4000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Main Socket successfully created")
try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))
s.listen()

s1 = server(4001,2)
s2 = server(4002,3)
s1.start()
s2.start()
sum_wt=s1.weight+s2.weight
wt=[]
i=0
while i<s1.weight:
    wt.append(1)
    i=i+1
i=0
while i<s2.weight:
    wt.append(2)
    i=i+1
while True:
    conn,addr=s.accept()
    ad=4000+wt[connum%sum_wt]
    connum=connum+1
    '''if ad==4002:
        ad=4000
    ad=ad+1'''
    ld=loadbalancer(conn,ad)
    ld.start()

