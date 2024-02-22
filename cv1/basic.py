import cv2 as cv

def rescaleFrame(frame, scale=.1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

img = cv.imread('photos/img2.jpg')
rs_img = rescaleFrame(img)

cv.imshow('Dogs', rs_img)

# Converting to grayscale
gray = cv.cvtColor(rs_img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(
    rs_img, # Image
    (9,9), # Blur Value
    cv.BORDER_DEFAULT
    )
# cv.imshow('Blur', blur)

# Edge Cascade
"""Using the blur image instead of rs_img reduces the number of edges in the image"""
canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

# Dilating the image
dilate = cv.dilate(canny, (3,3), iterations=4)
# cv.imshow('Dilated', dilate)

# Eroding the image
eroded = cv.erode(dilate, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resized)

# Cropping
cropped = img[300:200, 200:400]
cv.imshow('Cropped', cropped)



cv.waitKey(0)