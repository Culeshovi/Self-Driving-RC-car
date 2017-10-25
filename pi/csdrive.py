import socket               # Import socket module
import cv2
import numpy as np
import time
import pickle
import RPi.GPIO as GPIO ## Import GPIO library


# Digital output pins for front motor
f_motor1 = 13 
f_motor2 = 15

f_motor_Vcc = 2
f_motor_G = 6

# Digital output pins for rear motor
r_motor1 = 16
r_motor2 = 18

GPIO.setwarnings(False) ## Ignores GPIO Warnings
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

GPIO.setup(f_motor1, GPIO.OUT)
GPIO.setup(f_motor2, GPIO.OUT)

GPIO.setup(r_motor1, GPIO.OUT)
GPIO.setup(r_motor2, GPIO.OUT)


def isstop():
    GPIO.output(r_motor1,True)
    GPIO.output(r_motor2,True)

    time.sleep(0.1)
    
def right():
    GPIO.output(f_motor1, True) # Front motor right
    GPIO.output(f_motor2, False)

    GPIO.output(r_motor1, True) # Rear motor front
    GPIO.output(r_motor2, False)

    time.sleep(0.1)

def left():
    GPIO.output(f_motor1, False) # Front motor left
    GPIO.output(f_motor2, True)

    GPIO.output(r_motor1, True) # Rear motor move front
    GPIO.output(r_motor2, False)

    time.sleep(0.1)

def forward():
    GPIO.output(f_motor1, False) # Front motor neutral
    GPIO.output(f_motor2, False)

    GPIO.output(r_motor1, True) # Rear motor move front
    GPIO.output(r_motor2, False)

    time.sleep(0.1)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # ipManSaysHi...Awwwwww, now lets have sex
port = 5555               # Reserve a port for your souerviccsse.
s.connect((host, port))
cap = cv2.VideoCapture(0)
while True:
	ret,frame=cap.read()
	rval,imgencode=cv2.imencode(".jpg",frame,[1,90])
	data1=pickle.dumps(imgencode) #Pickkkkkyyyyyyyyyyyyyyy..........Yahoooooooooooooooooo
	s.sendall(data1)
	k=s.recv(1024)
	k=k.decode('utf-8')
	if (k=='D'):
        right()
    elif (k=='A'):
        left()
    elif (k=='W'):
        forward()
    else:
        isstop()
            
            
    GPIO.cleanup()
cap.release()
s.close()


