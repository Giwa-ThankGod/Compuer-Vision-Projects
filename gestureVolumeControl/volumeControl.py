import time
import math
import cv2 as cv
import numpy as np

# ----------------------------------------------------------------------------------
# Components for volume control
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
# print(volRange)
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0
# ----------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------
# Allows us to import files/modules in sub_directories.
import sys
sys.path.insert(0, r'C:\Users\user\Desktop\CVision')
from handDetection.hand_tracking_module import handDetector
#-----------------------------------------------------------------------------------

wCam, hCam = 648, 488
pTime = 0

cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = handDetector()

while cap.isOpened():
    success, frame = cap.read()
    frame = detector.findHands(frame)
    lmlist = detector.findPosition(frame)

    if len(lmlist) > 0:
        # print(lmlist[4], lmlist[8])

        x1, y1 = lmlist[4][1], lmlist[4][2]  # Thumb Finger.
        x2, y2 = lmlist[8][1], lmlist[8][2]  # Index Finger.
        cx, cy = (x1 + x2)//2, (y1 + y2)//2  

        # Identifying both fingers.
        cv.circle(frame, (x1,y1), 15, (0,255,255), cv.FILLED)
        cv.circle(frame, (x2,y2), 15, (0,255,255), cv.FILLED)

        cv.line(frame, (x1,y1),(x2,y2), (255,0,255), 2)
        cv.circle(frame, (cx,cy), 15, (255,0,255), cv.FILLED)

        # Gets the distance between the two fingers.
        length = math.hypot(x2-x1,y2-y1)

        # Hand Range 50 - 200
        # Volume Range -65 - 0

        vol = np.interp(length, [50,200], [minVol, maxVol])  # converts hand range to vol range.
        volBar = np.interp(length, [50,200], [400, 150])  # converts hand range to volBar range.
        volPer = np.interp(length, [50,200], [0, 100])  # converts hand range to volPer range.
        
        volume.SetMasterVolumeLevel(vol, None)

        if length<50:
            cv.circle(frame, (cx,cy), 15, (0,255,0), cv.FILLED)

    # Volume Bar
    cv.rectangle(frame, (50,150),(85,400), (0,255,0), 2) # 0%
    cv.rectangle(frame, (50, int(volBar)),(85,400), (0,255,0), cv.FILLED)  # 100%

    cv.putText(frame, f"VOL : {int(volPer)}%", (15,450), cv.FONT_HERSHEY_PLAIN, 1.5, (0,255,0), 2)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(frame, f"FPS : {int(fps)}", (40,50), cv.FONT_HERSHEY_PLAIN, 1.5, (0,255,0), 2)

    cv.imshow("frame", frame)
    
    if cv.waitKey(1) & 0xff==ord('q'):
        break