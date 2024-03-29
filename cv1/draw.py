import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

# cv.imshow('Blank Image', blank)

# 1. Point the image a certain colour
# blank[:] = 0,225,255 # Color scheme
# cv.imshow('Blank Yellow Image', blank)


# blank[200:300, 200:300] = 0,255,255
# cv.imshow('Yellow Square', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
# cv.imshow('Rectangle', blank)

# 2. Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,255), thickness=2)
# cv.imshow('Circle', blank)

# 3. Draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,255), thickness=2)
# cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)
