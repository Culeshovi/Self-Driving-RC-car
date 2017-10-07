import cv2
import os
cap = cv2.VideoCapture(0) #If webcam does'nt work set it to -1 or 1
count=0
path_output_dir='\data'
e1 = cv2.getTickCount()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    cv2.imwrite(os.path.join(path_output_dir,"frame%d.jpg")%count,frame)
    count+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
	e2 = cv2.getTickCount()
	t = (e2 - e1)/cv2.getTickFrequency()
	print (1.0/t)
# When everything done, release the capture
<<<<<<< HEAD
cap.release()
cv2.destroyAllWindows()
=======
cap.release() 
cv2.destroyAllWindows()
>>>>>>> 2a95922f2b6071073658b482eb57a97bad1ba33e
