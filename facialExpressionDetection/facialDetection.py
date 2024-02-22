import time
import cv2 as cv
import numpy as np
import math

# Allows us to import files/modules in sub_directories.
#----------------------------------------------------------------------
import sys
sys.path.insert(0, r'C:\Users\user\Desktop\CVision')
from faceMesh.face_mesh_module import FaceMeshDetector
from faceDetection.face_module import FaceDetector
#----------------------------------------------------------------------

def main():
    cap = cv.VideoCapture(0)
    smileBar = 400
    smilePer = 0
    pTime = 0
    mesh_detector = FaceMeshDetector()
    face_detector = FaceDetector()
    while True:
        success, frame = cap.read()
        # frame, faceLms = mesh_detector.drawMesh(frame,label=True)
        frame, bbox = face_detector.findFace(frame)
        h, w, c = frame.shape

        # print(frame.shape)
        cv.rectangle(frame, (0,h-50), (50,h), (0,255,0), cv.FILLED)
        cv.putText(frame, "2", ((h-50)//2, (h+50)//2), cv.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
        if len(bbox) > 0:
            pass

        # if len(faceLms) > 0:
        #     # Smile Points : 37 and 267
        #     id1, x1, y1 = faceLms[0][254]
        #     id2, x2, y2,= faceLms[0][282]
        #     pt1 = (int(x1), int(y1))
        #     pt2 = (int(x2), int(y2))

        #     cv.line(frame, pt1, pt2, (255,0,255), 2)

        #     length = math.hypot(x2-x1,y2-y1)
        #     print(length)

        #     # Smile Range 102 - 544
        #     smileBar = np.interp(length, [16,114], [400, 150])
        #     smilePer = np.interp(length, [16,114], [0, 100])

        #     # Volume Bar
        # cv.rectangle(frame, (50,150),(85,400), (0,255,0), 2) # 0%
        # cv.rectangle(frame, (50, int(smileBar)),(85,400), (0,255,0), cv.FILLED)  # 100%

        # cv.putText(frame, f"Mood : {int(smilePer)}%", (15,450), cv.FONT_HERSHEY_PLAIN, 1.5, (0,255,0), 2)        

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv.putText(frame, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)
        
        cv.imshow("Image", frame)

        if cv.waitKey(15) & 0xff==ord('q'):
            break


if __name__ == "__main__":
    main()