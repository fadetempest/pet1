import cv2 as cv
import numpy as np

img = cv.imread('images/rengar.jpeg')

def resize_img(frame, scale = 0.5):
    
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_CUBIC)

img_res = resize_img(img, scale=0.25)

cv.imshow("rengar", img_res)

# Split color channels

b,g,r = cv.split(img_res)

cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

cv.waitKey(0)