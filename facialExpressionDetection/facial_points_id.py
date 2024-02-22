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

def rescaleFrame(frame, scale=1):
    # Images, Video and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

IMG = r'images/img3.jpg'
detector = FaceMeshDetector(static_image_mode=True)
# face_detector = FaceDetector()

frame = cv.imread(IMG)
# frame = rescaleFrame(frame)
frame, faceLms = detector.drawMesh(frame)
# frame, bbox = face_detector.findFace(frame)

# Smile Range 37 - 267
id1, x1, y1 = faceLms[0][254]
id2, x2, y2,= faceLms[0][282]

# print(faceLms[0][57])
# print(faceLms[0][282])

# length = math.hypot(x2-x1,y2-y1)
# print(length)

cv.circle(frame, (x1,y1), 15, (0,255,255), cv.FILLED)
cv.circle(frame, (x2,y2), 15, (0,255,255), cv.FILLED)
cv.line(frame,(x1,y1),(x2,y2),(0,255,0),2)
cv.imshow("img", frame)
# cv.imwrite("images/eye2.jpg", frame)

cv.waitKey(0)
cv.destroyAllWindows()