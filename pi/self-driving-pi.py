import RPi.GPIO as GPIO ## Import GPIO library
import time
import cv2

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
    pass

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
    

def main():
    selfcar=True
    k=-1
    while (selfcar):
        if (k==0):
            right()
        elif (k==1):
            left()
        elif (isstop()):
            GPIO.output(ardystop,True)
        else:
            GPIO.output(ardystop,False)
            forward()
            print("Partttyyyyy")
    
            
    GPIO.cleanup()

if __name__ == '__main__':
    main()
