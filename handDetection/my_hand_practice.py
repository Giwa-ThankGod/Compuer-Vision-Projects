import time
import cv2 as cv
import hand_tracking_module as htm

def main():
    pTime = 0
    cTime = 0

    # Using our designed module
    detector = htm.handDetector()

    capture = cv.VideoCapture(0)

    while capture.isOpened():
        # capture frame by frame
        success, frame = capture.read()

        frame = detector.findHands(frame)

        lmlist = detector.findPosition(frame)
        if len(lmlist) != 0:
            print(lmlist[0])


        # CALCULATING FRAME RATE
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv.putText(frame, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)    

        cv.imshow('Frame', frame)

        # stops the video from playing indefinitely, 
        if cv.waitKey(20) & 0xff==ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()