import socket
import threading
import time

HOST = "2401:4900:314a:79e5:5ddb:581e:bf1a:f59a"
PORT = 8734

ADDR = (HOST,PORT)

server = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)

server.bind(ADDR)



ad = []
x = ""
y = ""
    

print("waiting for the connections")
server.listen(4)

while True:
    for i in range(3):
        conn, addr = server.accept()
        ad.append(conn)
        
        print("Connected with ",addr)
        conn.send(bytes("welcome to Chatter","utf-8"))
    
            

        def receive1():
            global x
            global y

            for j in range(7667):
                try:
                    x = ad[0].recv(1024)
                    #x = repr(data1)
                    
                except:
                    pass
                            
                
                
                time.sleep(1)
                    
        def send1():
            global x
            global y
                
            for i in range(7667):
                while x != "":        
                    try:

                        ad[1].send(bytes(x.decode(),"utf-8"))
                        x = ""

                    except:
                        pass
                       
                time.sleep(1)


        def receive2():
            global x
            global y

            for j in range(7667):
                
                try:
                    y = ad[1].recv(1024)
                    #y = repr(data1)
                    
                except:
                    pass
                            
                
                
                time.sleep(1)


        def send2():
            global x
            global y
                
            for i in range(7667):
                while y!= "":        
                    try:
                    
                        ad[0].send(bytes(y.decode(),"utf-8"))
                        y = ""
                    except:
                        pass
                time.sleep(1)
            
            
            
        
        threading.Thread(target = receive1).start()
        threading.Thread(target = send1).start()
        threading.Thread(target = receive2).start()
        threading.Thread(target = send2).start()
            
    
print("starting the server")






