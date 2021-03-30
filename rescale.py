import cv2 as cv
import numpy as np

# Reading images
img = cv.imread('Resources/Photos/cat_large.jpg')
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
# cv.imshow('Cat',img)
def rescaleFrame(frame,scale=0.75): # Works for photos, videos, live videos

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
def changeRes(width,height): # Works only for live videos
    capture.set(3,width) # 3 shows width
    capture.set(4,height) # 4 shows height
resized_img = rescaleFrame(img,0.20)
cv.imshow('Cat',img)
cv.imshow('Resized Image',resized_img)
cv.waitKey(0)


# Reading videos
# capture = cv.VideoCapture('Resources/Videos/dog.mp4')
# while True:
#     isTrue,frame = capture.read()
#     frame_resized = rescaleFrame(frame,0.25)
#     cv.imshow('Original video',frame)
#     cv.imshow('Resized video',frame_resized)
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

