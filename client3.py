import socket              
from tkinter import *
def conToServer():
    s = socket.socket()          
    conport=12345
    fname=e1.get()
    try:
        s.connect(('localhost',conport))
    except socket.error as e:
        print(str(e))
    s.send(fname.encode())
    data=s.recv(1024)
    if data.decode()=="File exist":
        m.set(data.decode())
        content=s.recv(1024)
        print(content.decode())
    else: m.set(data.decode())
    s.close()
root = Tk(className='Client Program 3')
root.geometry("400x400")
canvas = Canvas(root, width = 300, height = 300)      
canvas.pack(side=TOP)      
img = PhotoImage(file="filesearch.png")      
canvas.create_image(60,20, anchor=NW, image=img)      
file_name = Label(root, text = "File name",font = "Helvetica 12 bold").place(x = 40, y = 220)   
e1 = Entry(root,width=35)
e1.place(x=150,y=220)
m=StringVar()
msg = Label(root, text = "",font = "Helvetica 12 bold",textvariable=m)
msg.place(x = 150, y = 280)   
b1 = Button(root, text='Search',font = "Helvetica 12 bold",height=3,width=25,relief="groove",command=lambda: conToServer())
b1.pack(side=LEFT,anchor="sw",padx=5, pady=5)
b2 = Button(root, text='Quit',font = "Helvetica 12 bold",height=3,width=25,relief="groove",command=root.quit)
b2.pack(side=LEFT,anchor="se", padx=5, pady=5)
root.mainloop()