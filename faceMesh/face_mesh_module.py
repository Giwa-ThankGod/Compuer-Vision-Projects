import time
import cv2 as cv
import mediapipe as np

class FaceMeshDetector:
    def __init__(self, static_image_mode=False, minDetection=0.5, minTracking=0.5):
        self.npFaceMesh = np.solutions.face_mesh
        self.npdraw = np.solutions.drawing_utils
        self.drawSpec = self.npdraw.DrawingSpec(color = (0,255,0), thickness=1, circle_radius=1)
        self.faceMesh = self.npFaceMesh.FaceMesh(
            static_image_mode = static_image_mode,
            max_num_faces = 2,
            min_detection_confidence = minDetection, 
            min_tracking_confidence = minTracking) # Calls the face mesh class.

    def drawMesh(self, frame, draw=True, conn=True, label=True):
        frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(frameRGB) #assign an rgb frame for face mesh landmark.
        
        faces= []

        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.npdraw.draw_landmarks(
                        frame, 
                        faceLms, 
                        self.npFaceMesh.FACEMESH_CONTOURS if conn else None,
                        self.drawSpec,
                        self.drawSpec,
                    ) # draw lines joining face ladmarks.

                facesMesh_landmark = []
                for id,lm in enumerate(faceLms.landmark):
                    # ih, iw, ic = frame.shape
                    # x, y = int(lm.x * iw), int(lm.y * ih)  # Converting the landmarks to pexel values.

                    # Display the id number of each points on the face.
                    # if label:
                    #     cv.putText(frame, f"{id}", (x,y), cv.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1)
                    
                    facesMesh_landmark.append([id,lm.x,lm.y])
                
                faces.append(facesMesh_landmark)

        return frame, faces