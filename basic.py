import cv2 as cv
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow("Cat",img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray image',gray)


# blur the image
blurImage = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blurImage)

# Edge Cascade
canny = cv.Canny(img,125,175)
cv.imshow("Canny Edges",canny)
canny = cv.Canny(blurImage,125,175)
cv.imshow("Canny Edges",canny)


# Dilating the image
dilated = cv.dilate(canny,(3,3),iterations=4)
cv.imshow("Dilated",dilated)
# Eroding
eroded = cv.erode(dilated,(3,3),iterations=3)
cv.imshow('Eroded',eroded)


# Resize 
resized = cv.resize(img,(500,500))
cv.imshow("Resized",resized)

# Crop
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)