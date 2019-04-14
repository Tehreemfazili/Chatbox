import socket
import sys
import time

s=socket.socket()
host = input(str("Please enter the hostname of the system"))
port =8080
s.connect((host,port))
print ("cconnected to the server")
while 1:
	incomming_message = s.recv(1024)
	incomming_message = incomming_message.decode()
	print("server", incomming_message)
	print("")
	message = input(str(">>"))
	message= message.encode()
	s.send(message)
	print("message has been sent")
	print("")



