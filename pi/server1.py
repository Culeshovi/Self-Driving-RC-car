import socket
import cv2
import numpy as np  
import pickle   
import os     # Import socket module
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() #ipManSaysHi...Awwwwww
port = 5555
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)
cap=cv2.VideoCapture(0)
c, addr = s.accept()     # Establish connection with client.
print ('Got connection from', addr) # Now wait for client connection.

while True:
	ret,frame=cap.read()
	rval,imgencode=cv2.imencode(".jpg",frame,[1,90])
	data1=pickle.dumps(imgencode) #Pickkkkkyyyyyyyyyyyyyyy..........Yahoooooooooooooooooo
	c.sendall(data1)
	k=c.recv(1024)
	print (k.decode('utf-8'))

c.close()
cv2.destroyAllWindows()      