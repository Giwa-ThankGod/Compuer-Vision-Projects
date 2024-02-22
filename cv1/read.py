import cv2 as cv

# Reading Images
# img = cv.imread('photos/img1.jpg')

# cv.imshow('Image', img)

# cv.waitKey(0)

#Reading Video Capture
capture = cv.VideoCapture('videos/vid1.mp4')

#Reads video frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    # stops the video from playing indefinitely, 
    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

