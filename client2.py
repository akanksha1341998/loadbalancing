import socket                
  
# Create a socket object 
s = socket.socket()          
conport=12345
#print("Connecting to port ",conport)
s.connect(('localhost',conport))
s.send("Hello I am client2\n".encode() )
data=s.recv(1024)
print(data.decode())
s.close()


