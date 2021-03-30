import cv2 as cv
import numpy as np
# img = cv.imread('Resources/Photos/cat_large.jpg')
# we can make a blank image
blank = np.zeros((500,500,3),dtype='uint8') # uint8 is data type of an image
# cv.imshow('Blank Image',blank)

# we can color the image

# blank[:] = 0,0,255 # paint into Red
# blank[200:300,300:400]=0,0,255 # We can paint a certain portain

# cv.imshow("Colored Image",blank)
# To draw a rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0))
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED) #thickness=-1 is same as thickness=cv.FILLED, it will fill the whole area

# cv.imshow('Rectangle',blank)

# Draw a circle
cv.circle(blank,(250,250),40,(0,0,255),thickness=-1) # here 40 is radius
# cv.imshow("Circle",blank)



# Draw a line
cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
# cv.imshow("Line",blank)

# Write text on image
cv.putText(blank,'Manzoor',(250,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Text',blank)

#
cv.waitKey(0)
