import socket
import sys, os
import threading

HOST = ''
PORT = 6789
   
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
try:
    soc.bind((HOST, PORT))
      
except socket.error as message:
    print('Bind failed. Error Code : '
          + str(message[0]) + ' Message '
          + message[1])
    sys.exit()
     

print('Start listening') 

soc.listen()
  

def HandleClient(conn, address):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        if(data == b"quit"):
            conn.close()
            os._exit(1)
        conn.sendall(data)
    


while True:
    conn, address = soc.accept()
    print('Client connected: ' + address[0] + ':' + str(address[1]))
    t = threading.Thread(target=HandleClient, args= (conn, address ))
    t.daemon = True
    t.start()


        