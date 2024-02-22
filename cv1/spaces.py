import cv2 as cv
import matplotlib.pyplot as plt

def rescaleFrame(frame, scale=.1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

img = cv.imread('photos/img1.jpg')
rs_img = rescaleFrame(img)

cv.imshow('Image', rs_img)

#View in Matplot
plt.imshow(rs_img)
plt.show()

# BGR to Grayscale
gray = cv.cvtColor(rs_img, cv.COLOR_BGR2GRAY)
# cv.imshow('GRAY', gray)

# BGR to HSV
hsv = cv.cvtColor(rs_img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(rs_img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)





cv.waitKey(0)