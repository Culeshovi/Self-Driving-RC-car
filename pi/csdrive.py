import socket               # Import socket module
import cv2
import numpy as np
import time
import pickle
import RPi.GPIO as GPIO ## Import GPIO library
import time
import cv2
import caret
delay = 5


f_motor1 = 13
f_motor2 = 15
f_motor_Vcc = 2
f_motor_G = 6
ardystop=32

GPIO.setwarnings(False) ## Ignores GPIO Warnings
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

GPIO.setup(f_motor1, GPIO.OUT)
GPIO.setup(f_motor2, GPIO.OUT)
GPIO.setup(ardystop, GPIO.OUT)

def getimage():
    #Getting Image from webcam
    frame=caret.capy()

def isstop():
    ardy=False
    getimage()
    #Junior's Code
    GPIO.output(ardystop, ardy)
    pass
    
def right():
    
    GPIO.output(f_motor1, True)
    GPIO.output(f_motor2, False)

    time.sleep(0.1)

def left():

    GPIO.output(f_motor1, False)
    GPIO.output(f_motor2, True)

    time.sleep(0.1)
def forward():
    GPIO.output(f_motor1, False)
    GPIO.output(f_motor2, False)

    time.sleep(0.1)

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
	k=k.decode('utf-8')
	if (k=='R'):
            right()
        elif (k=='L'):
            left()
        elif (isstop()):
            GPIO.output(ardystop,True)
        else:
            GPIO.output(ardystop,False)
            forward()
            print("Partttyyyyy")
    GPIO.cleanup()
cap.release()
s.close()



