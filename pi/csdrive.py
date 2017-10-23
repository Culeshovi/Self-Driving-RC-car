import socket               # Import socket module
import cv2
import numpy as np
import time
import pickle
import RPi.GPIO as GPIO ## Import GPIO library
import caret
delay = 5


f_motor1 = 13
f_motor2 = 15
f_motor_Vcc = 2
f_motor_G = 6
ardystop=36
r_motor=32

GPIO.setwarnings(False) ## Ignores GPIO Warnings
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

GPIO.setup(f_motor1, GPIO.OUT)
GPIO.setup(f_motor2, GPIO.OUT)
GPIO.setup(ardystop, GPIO.OUT)
GPIO.setup(r_motor,GPIO.OUT)
pwm=GPIO.PWM(32,100)

def isstop():
    GPIO.output(r_motor,False)
    time.sleep(0.1)
    
def right():
    pwm.start(60)
    GPIO.output(f_motor1, True)
    GPIO.output(f_motor2, False)
    GPIO.output(r_motor, True)
    time.sleep(0.1)
    pwm.stop()

def left():
    pwm.start(60)
    GPIO.output(f_motor1, False)
    GPIO.output(f_motor2, True)
    GPIO.output(r_motor, True)
    time.sleep(0.1)
    pwm.stop()
def forward():
    pwm.start(40)
    GPIO.output(f_motor1, False)
    GPIO.output(f_motor2, False)
    GPIO.output(r_motor, True)
    time.sleep(0.1)
    pwm.stop()

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



