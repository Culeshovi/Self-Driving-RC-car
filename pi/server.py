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
count=0  
path_output_dir='/home/culeshovi/Desktop/'
c, addr = s.accept()     # Establish connection with client.
print ('Got connection from', addr) # Now wait for client connection.
while True:
	print('W,S,A,D')#W,S,A,D
	k=input("Enter Commando") 
	c.sendall(str.encode(k))
	data=c.recv(1024*1024)
	data=pickle.loads(data)
	dec=cv2.imdecode(data,1)
	cv2.imshow('frame2',dec)
	cv2.imwrite(os.path.join(path_output_dir+k,"frame%d.jpg")%count,dec)
	count+=1
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
c.close()
cv2.destroyAllWindows()      