import cv2 as cv

def rescaleFrame(frame, scale=.1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

img = cv.imread('photos/img3.jpg')
rs_img = rescaleFrame(img)

cv.imshow('Image', rs_img)



cv.waitKey(0)