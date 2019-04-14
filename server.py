import socket
import sys
import time

s=socket.socket()
host = socket.gethostname()
print("server willstart on host: ", host)
port =  8080
s.bind((host,port))
print("")
print("server is waiting for incoming connection")
print("")
s.listen(1)
conn.addr = s.accept()
print(addr,"has connected to the server and is now online")
print("")
while 1:
	message = input(str(">>"))
	message= message.encode()
	conn.send(message)
	print("messagehas been sent")
	print("")
	incomming_message = conn.recv(1024)
	incomming_message = incomming_message.decode()
	print("client", incomming_message)
	print("")
