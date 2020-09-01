import socket
import threading
import time
from tkinter import *

chatter = Tk()
chatter.title("Subtle Chat")
chatter.geometry("350x500")

sb = Scrollbar(chatter)  
sb.pack(side = RIGHT, fill = Y) 
fchats = Frame()
fchats.pack(expand=True,anchor="n")
ftext = Frame()
ftext.pack(fill=X)
recvar = StringVar()
senvar = StringVar()

label_rec = Label(master = fchats,text= "Welcome to Subtle Chat created by The legendary Veer" ,  fg="red")
label_rec.pack(anchor="n")


 

#mylist = Listbox(fchats, yscrollcommand = sb.set )  
#mylist.pack()
textbox = Entry(ftext,textvariable= senvar)
textbox.pack(fill=X)

sendbutt = Button(text="send",command=lambda:send2())
sendbutt.pack()
     
  
  

sb.config( command = fchats )




HOST = socket.gethostbyname(socket.gethostname)
PORT = 8734

ADDR = (HOST,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ADDR)




    
def receive2():
    for j in range(7667):
        x = client.recv(1024)
        recvar.set(repr(x))

        
        #if recvar.get() in mylist.get(first=0):
            #pass
        # else:  
    
           # mylist.insert(END,recvar.get()) 
        rec_label = Label(master=fchats,text= recvar.get() , bg= "black" , fg="white")
        rec_label.pack(anchor="w")


checklist =[]
def send2():
    global checklist
    
    
    
    if senvar.get() in checklist:
        pass
    else:
        client.send(bytes(senvar.get(),"utf-8"))
        send_label = Label(master =fchats,text=senvar.get() ,bg="#054640" ,fg ="white")
        send_label.pack(anchor="e")
        
        checklist.append(senvar.get())
        client.send(bytes(senvar.get(),"utf-8"))
        senvar.set("")

    
        

threading.Thread(target = receive2).start() 
#threading.Thread(target = send2).start()
chatter.mainloop()