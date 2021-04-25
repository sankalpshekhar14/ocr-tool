def process_par(img):	
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,th = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	# assign a rectangle kernel size
	kernel = np.ones((5,5), 'uint8')	
	par_img = cv2.dilate(th,kernel,iterations=3)
	
	(contours, _) = cv2.findContours(par_img.copy(),cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	
	for cnt in contours:
		x,y,w,h = cv2.boundingRect(cnt)
		if(w<20 or h<20): continue
		cv2.rectangle(output,(x,y),(x+w,y+h),(0,255,0),1)
	return img

def process_margin(img):	
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,th = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	# assign a rectangle kernel size
	kernel = np.ones((20,5), 'uint8')	
	margin_img = cv2.dilate(th,kernel,iterations=5)
	
	(contours, _) = cv2.findContours(margin_img.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	
	for cnt in contours:
		x,y,w,h = cv2.boundingRect(cnt)
		if(w<30 or h<30): continue
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)

	return img