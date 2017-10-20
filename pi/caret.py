import cv2
def capy():
	cap = cv2.VideoCapture(0) #If webcam does'nt work set it to -1 or 1
	count=0
	while(True):
    # Capture frame-by-frame
		ret, frame = cap.read()
    
		return frame
		count+=1
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()

