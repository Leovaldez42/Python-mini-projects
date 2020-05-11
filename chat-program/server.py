import socket
import sys
import time

s = socket.socket()
host = socket.gethostname()
print("sever will start on host: ", host)
port = 8080
s.bind((host, port))
print("")
print("server done binding to host and port successfully")
print("")
print("server is wauting for incomming connections")
s.listen(1)
conn, addr = s.accept()
print(addr, "has connected tot he server and is now online")
print("")
while 1:
    message = input(str(">> "))
    message = message.encode()
    conn.send(message)
    print("message has been sent...")
    print("")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server: ", incoming_message)
    print("")
    
# How to use this application
# 1) run server.py
# 2) run client.py while keeping the server.py file running
# 3) Copy the hostname displayed on the console of server.py and paste it on the input of "Please enter hostname of the server: "
# 4) Start typing messages