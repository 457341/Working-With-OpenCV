import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 
import numpy as np
img = cv.imread('Resources/Photos/park.jpg')
blank  = np.zeros(img.shape[:2],dtype='uint8')

cv.imshow("Image",img)
b,g,r = cv.split(img)
cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)
print(img.shape)
print(b.shape)
print(g.shape)
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

print(r.shape)
merged = cv.merge([b,g,r])
cv.imshow('Merged Image',merged)
cv.imshow("Blue",blue)
cv.imshow("Red",red)
cv.imshow("Green",green)
cv.waitKey(0)