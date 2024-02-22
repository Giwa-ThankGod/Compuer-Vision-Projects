import cv2 as cv
import numpy as np
import time
import math

# Allows us to import files/modules in sub_directories.
#----------------------------------------------------------------------
import sys
sys.path.insert(0, r'C:\Users\user\Desktop\CVision')
from poseDetection.pose_module import poseDetector
#----------------------------------------------------------------------

def exercise_count(frame, foot, per, bar, count, dir):
    """
    Calculate the Number of correct exercise done.
    Returns the number of count and the direction of the percentage: 0% / 100%"""

    if int(per) == 100 and dir == 0:
        count += .5
        dir = 1

        if foot:  
            cv.rectangle(frame, (450, int(bar)),(485,650), (255,255,255), cv.FILLED)  # RIGHT FOOT
        else:
            cv.rectangle(frame, (50, int(bar)),(85,650), (255,255,255), cv.FILLED)  # LEFT FOOT
    
    if int(per) == 0 and dir == 1:
        count += .5
        dir = 0

        if foot:  
            cv.rectangle(frame, (450, int(bar)),(485,650), (255,255,255), cv.FILLED)  # RIGHT FOOT
        else:
            cv.rectangle(frame, (50, int(bar)),(85,650), (255,255,255), cv.FILLED)  # LEFT FOOT
    
    return count, dir

def main():
    leftCount = 0
    leftDir = 0

    rightCount = 0
    rightDir = 0

    cap = cv.VideoCapture('videos/pose/vid3.mp4')

    # wCam, hCam = 540, 960
    # cap.set(3, wCam)
    # cap.set(4, hCam)

    pTime = 0
    detector = poseDetector()
    while True:
        success, frame = cap.read()
        frame = detector.findPose(frame, drawConn=False)
        lmList = detector.findPostion(frame, draw=False, label=False)

        # cv.rectangle(frame, (50,170),(85,650), (255,255,255), 2) # 0%
        # cv.rectangle(frame, (450,170),(485,650), (255,255,255), 2) # 0%

        if len(lmList) > 0:
            leftFoot = detector.findAngle(frame, 23,25,27, (255,0,0))
            rightFoot = detector.findAngle(frame, 24,26,28, (255,0,255))

            x1, y1 = lmList[27][1], lmList[27][2]
            x2, y2 = lmList[28][1], lmList[28][2]
            cv.line(frame, (x1,y1),(x2,y2), (255,0,255), 2)
            length = math.hypot(x2-x1,y2-y1)
            print(length)


            # Volume Bar
            leftBar = np.interp(leftFoot, [200,289], [650, 170])
            rightBar = np.interp(rightFoot, [200,289], [650, 170])
            # Percent Bar
            leftPer = np.interp(leftFoot, [200,289], [0, 100])
            rightPer = np.interp(rightFoot, [200,289], [0, 100])

            # LEFT FOOT
            cv.putText(frame, f"{int(leftCount)}", (50,140), cv.FONT_HERSHEY_PLAIN, 1.5, (255,255,0), 2)
            cv.rectangle(frame, (50,170),(85,650), (255,255,255), 2) # 0%
            cv.rectangle(frame, (50, int(leftBar)),(85,650), (255,255,0), cv.FILLED)  # 100%
            cv.putText(frame, f"{int(leftPer)}%", (50,680), cv.FONT_HERSHEY_PLAIN, 1, (255,255,0), 2)
            cv.putText(frame, f"Left Foot", (30,720), cv.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)

            # RIGHT FOOT
            cv.putText(frame, f"{int(rightCount)}", (450,140), cv.FONT_HERSHEY_PLAIN, 1.5, (255,255,0), 2)
            cv.rectangle(frame, (450,170),(485,650), (255,255,255), 2) # 0%
            cv.rectangle(frame, (450, int(rightBar)),(485,650), (255,255,0), cv.FILLED)  # 100%
            cv.putText(frame, f"{int(rightPer)}%", (450,680), cv.FONT_HERSHEY_PLAIN, 1, (255,255,0), 2)
            cv.putText(frame, f"Right Foot", (430,720), cv.FONT_HERSHEY_PLAIN, 1, (255,255,255), 2)


            leftCount, leftDir =  exercise_count(frame, 0, leftPer, leftBar, leftCount, leftDir)
            rightCount, rightDir =  exercise_count(frame, 1, rightPer, rightBar, rightCount, rightDir)


        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv.putText(frame, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)

        cv.namedWindow("reframed", cv.WINDOW_NORMAL)
        cv.resizeWindow("reframed", 540, 960)
        cv.imshow("reframed", frame)

        # cv.imshow("reframed", frame)
        if cv.waitKey(30) & 0xff==ord('q'):
            break
        
    cv.destroyWindow("reframed")
    cv.destroyAllWindows()     
    cap.release()


if __name__ == "__main__":
    main()