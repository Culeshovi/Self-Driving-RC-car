import cv2
import numpy as np
from getkeys import getKey
import os



starting_value = 1

while True:
    file_name = 'training_data-{}.npy'.format(starting_value)

    if os.path.isfile(file_name):
        print('File exists, moving along',starting_value)
        starting_value += 1
    else:
        print('File does not exist, starting fresh!',starting_value)
        break
        

cap=cv2.VideoCapture(1)
while True:
	training_data=[]
	ret,frame=cap.read()
	screen=cv2.resize(frame, (128,128))
	cv2.imshow('frame',frame)
	key=getKey()
	training_data.append([screen,key])
	
	if key=='x':
		np.save(file_name,training_data)
		print('SAVED')
		training_data = []
		starting_value += 1
		file_name = '/media/culeshovi/New Volume/Souvik/machine learning/openCV/training_data-{}.npy'.format(starting_value)
		break
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
cap.release()
cv2.destroyAllWindows()




