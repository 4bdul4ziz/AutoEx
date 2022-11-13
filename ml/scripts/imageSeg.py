
import cv2
import numpy as np

#read the image
#HMM YES INTERESTING IMAGE
image = cv2.imread('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/written/IMG_6024.jpg')
#convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#binary
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#dilation
kernel = np.ones((5,100), np.uint8)
#DILAAAAAATEEEE SKREEEEEEEEEEE
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
#find contours
ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
#crop each word and save it to a folder
for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)
    # Getting ROI
    roi = image[y:y+h, x:x+w]
    # show ROI
    #i need therapy
    cv2.imshow('segment no:'+str(i),roi)
    cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2)
    #rectangle cause cool
    cv2.waitKey(0)
    #save each word as a separate image
    cv2.imwrite('/Users/abdul/Desktop/Programming/R Programs/AutoEx/ml/data/segments/word'+str(i)+'.png', roi)

cv2.imshow('marked areas',image)
cv2.waitKey(0)





