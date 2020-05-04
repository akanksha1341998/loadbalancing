import socket                
  
# Create a socket object 
s = socket.socket()          
conport=12345
#print("Connecting to port ",conport)
try:
    s.connect(('localhost',conport))
except socket.error as e:
    print(str(e))
s.send("Hello I am client\n".encode() )
data=s.recv(1024)
print(data.decode())
s.close()

