import cv2 as cv

#Reading Video Capture
capture = cv.VideoCapture(1)

#Reads video frame by frame
while True:
    isTrue, frame = capture.read()

    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier(cv.samples.findFile(r"haar_cascade/haarcascade_frontalface_default.xml"))

    faces_rect = haar_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=1)

    for (x,y,w,h) in faces_rect:
        cv.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0,255,0),
            2 
            )

    cv.imshow('Video', frame)

    # stops the video from playing indefinitely, 
    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

