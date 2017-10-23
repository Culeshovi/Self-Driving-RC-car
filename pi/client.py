import socket               # Import socket module
import cv2
import numpy as np
import time
import pickle
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # ipManSaysHi...Awwwwww
port = 5555               # Reserve a port for your service.
s.connect((host, port))
cap=cv2.VideoCapture(0)
while True:
	ret,frame=cap.read()
	rval,imgencode=cv2.imencode(".jpg",frame,[1,90])
	data1=pickle.dumps(imgencode) #Pickkkkkyyyyyyyyyyyyyyy..........Yahoooooooooooooooooo
	s.sendall(data1)
	k=s.recv(1024)
	print (k.decode('utf-8'))
cap.release()
s.close()



