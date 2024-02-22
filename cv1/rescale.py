import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Images, Video and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def changeResolution(width, height):
    # Only works on Live Video
    capture.set(3, width)
    capture.set(4, height)

img = cv.imread('photos/img1.jpg')

resized_img = rescaleFrame(img, scale=.15)

cv.imshow('Image', resized_img)

# Reads Video
capture = cv.VideoCapture('videos/vid1.mp4')

#Reads video frame by frame
while True:
    isTrue, frame = capture.read()

    changeResolution(620, 480)

    frame_resized = rescaleFrame(frame)

    # cv.imshow('Video', frame)
    cv.imshow('Video', frame_resized)

    # stops the video from playing indefinitely, 
    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()