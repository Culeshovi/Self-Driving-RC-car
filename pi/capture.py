import cv2
import numpy as np
import os
cap = cv2.VideoCapture(1) #If webcam does'nt work set it to -1 or 1
count=0
path_output_dir='\data'
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imwrite(os.path.join(path_output_dir,"frame%d.jpg")%count,frame)
    count+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release() 
cv2.destroyAllWindows()
