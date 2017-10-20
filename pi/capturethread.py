import cv2
import os
from imutils.video import WebcamVideoStream
import imutils

cap = WebcamVideoStream(src=0).start()#If webcam does'nt work set it to -1 or 1
count=0
path_output_dir='/home/culeshovi/Self-Driving-RC-car/pi/data'
e1 = cv2.getTickCount()
while(True):
    # Capture frame-by-frame
    frame = cap.read()
    
    cv2.imwrite(os.path.join(path_output_dir,"frame%d.jpg")%count,frame)
    count+=1
    if count==1500:
        break 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    e2=cv2.getTickCount()
    
# When everything done, release the capture
t = (e2 - e1)/cv2.getTickFrequency()
print (t)
cap.stop()
cv2.destroyAllWindows()
