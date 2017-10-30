import socket               # Import socket module
import cv2
import numpy as np
import time
import pickle
import os

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # ipManSaysHi...Awwwwww
port = 5555               # Reserve a port for your service.
s.connect((host, port))
count=0  
path_output_dir='/home/culeshovi/Desktop/'
cap=cv2.VideoCapture(0)
while True:
	data=s.recv(1024*1024)
	data=pickle.loads(data)
	dec=cv2.imdecode(data,1)
	cv2.imshow('frame2',dec)
	#cv2.imwrite(os.path.join(path_output_dir+k,"frame%d.jpg")%count,dec)
	print('W,S,A,D')#W,S,A,D
	k=input("Enter Commando") 
	s.sendall(str.encode(k))
	count+=1
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
s.close()



