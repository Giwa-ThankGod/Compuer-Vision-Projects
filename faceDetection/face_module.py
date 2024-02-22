import time
import cv2 as cv
import mediapipe as np

class FaceDetector:
    def __init__(self, minDetection=0.5):
        self.npFaceDetection = np.solutions.face_detection
        self.npdraw = np.solutions.drawing_utils
        self.faceDetection = self.npFaceDetection.FaceDetection() # Calls the face detection class.

    def findFace(self, frame, draw=True):
        frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(frameRGB) #assign an rgb frame for face detection.
        
        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                # self.npdraw.draw_detection(frame, detection) # mediapipe built-in face draw.
                
                bboxC = detection.location_data.relative_bounding_box # Grabs the corners of the face.
                h, w, c = frame.shape # Grabs frame dimension.

            
                bbox = int(bboxC.xmin * w), int(bboxC.ymin * h), \
                    int(bboxC.width * w), int(bboxC.height * h) # Get actual corners of the face on the frame.
                area = (w-bbox[2]) * (h-bbox[3])
                area = int(area/1000)
                
                bboxs.append([id, bbox, area, detection.score])

                if draw:
                    frame = self.fancyDraw(frame, bbox)
                    detection_score = int(detection.score[0]*100)

                    cv.putText(
                        frame, 
                        str(f"{detection_score}%"), 
                        (bbox[0], bbox[1] - 50), 
                        cv.FONT_HERSHEY_PLAIN,
                        1.5, (0,255,0), 2
                    )
                    cv.putText(
                        frame, 
                        str(f"FaceID : {id+1}"), 
                        (bbox[0], bbox[1] - 20), 
                        cv.FONT_HERSHEY_PLAIN,
                        1.5, (0,255,0), 2
                    )
                    
        return frame, bboxs
    

    def fancyDraw(self, frame, bbox, lenght = 30, thickness= 3):
        x, y, w, h = bbox
        x1, y1 = x+w, y+h
        
        # cv.rectangle(frame, bbox, (0,255,0), 2)
        # Top Left
        cv.line(frame, (x,y),(x+lenght,y), (0,255,0),thickness) 
        cv.line(frame, (x,y),(x,y+lenght), (0,255,0),thickness)
        # Top Right
        cv.line(frame, (x1,y),(x1-lenght,y), (0,255,0),thickness) 
        cv.line(frame, (x1,y),(x1,y+lenght), (0,255,0),thickness)

        # Bottom Left
        cv.line(frame, (x,y1),(x+lenght,y1), (0,255,0),thickness) 
        cv.line(frame, (x,y1),(x,y1-lenght), (0,255,0),thickness)
        # Bottom Right
        cv.line(frame, (x1,y1),(x1-lenght,y1), (0,255,0),thickness)
        cv.line(frame, (x1,y1),(x1,y1-lenght), (0,255,0),thickness)
        
        return frame

def main():
    cap = cv.VideoCapture(0)
    pTime = 0
    detector = FaceDetector()
    while True:
        success, frame = cap.read()
        frame, bboxs = detector.findFace(frame)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv.putText(frame, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)
        
        cv.imshow("Image", frame)

        if cv.waitKey(15) & 0xff==ord('q'):
            break


if __name__ == "__main__":
    main()