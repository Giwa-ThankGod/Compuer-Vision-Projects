import cv2
import time
from pose_module import poseDetector

def main():
    cap = cv2.VideoCapture('videos/pose/vid5.mp4')
    pTime = 0
    detector = poseDetector()
    while True:
        success, frame = cap.read()

        frame = detector.findPose(frame)
        print(frame.shape)
        lmlist = detector.findPostion(frame, draw=False)
        
        if len(lmlist) != 0:
            # print(lmlist[14]) #access mark for right elbow
            cv2.circle(frame, (lmlist[14][1], lmlist[14][2]), 15, (0,255,0), cv2.FILLED)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(frame, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)
        
        cv2.imshow("Image", frame)

        if cv2.waitKey(1) & 0xff==ord('q'):
            break

    cap.release()

if __name__ == "__main__":
    main()