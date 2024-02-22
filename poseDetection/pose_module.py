import cv2 as cv
import mediapipe as np
import math

class poseDetector:
    """Detects and Identify the landmarks on a human body."""
    def __init__(self, mode=False, upbody=False, smooth=True, detectionCon=0.8, trackingCon=0.5):
        self.mode = mode
        self.upbody = upbody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon
        
        self.npDraw = np.solutions.drawing_utils
        self.npPose = np.solutions.pose
        self.pose = self.npPose.Pose() # Passing the arguments result to an error.

    def findPose(self, frame, drawConn=True):
        """Find the landmark in a human body.
           Returns the frame with the detected landmarks.
        """
        frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(frameRGB)

        if self.results.pose_landmarks:
            if drawConn:
                self.npDraw.draw_landmarks(frame, self.results.pose_landmarks, self.npPose.POSE_CONNECTIONS)

        return frame

    def findPostion(self, frame, draw=True, label=True):
        """Returns a landmark list of positions in a human body"""
        self.lmlist = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = frame.shape # Grab the dimension of the frame.
                cx, cy = int(lm.x * w), int(lm.y * h) # Locate the marks on the frame.
                self.lmlist.append([id,cx,cy])
                # print(lm.x, lm.y)
                # print(cx, cy)
                if draw:
                    cv.circle(frame, (cx, cy), 5, (255,0,0), cv.FILLED)

                # Display the id number of each points on the face.
                if label:
                    cv.putText(frame, f"{id}", (cx+10,cy+10), cv.FONT_HERSHEY_PLAIN, 1, (0,255,0), 2)
                
        return self.lmlist
    
    def findAngle(self, frame, pt1, pt2, pt3, color,draw=True):
        """Returns the angle between the points given"""

        # Get the landmarks
        x1, y1 = self.lmlist[pt1][1:]
        x2, y2 = self.lmlist[pt2][1:]
        x3, y3 = self.lmlist[pt3][1:]

        # Get the angle
        angle = math.degrees(
            math.atan2(y3-y2,x3-x2) - math.atan2(y1-y2,x1-x2)
        )

        # Converts negative angles to positive.
        if angle < 0:
            angle += 360 
        

        # Draw
        if draw:
            # X1
            cv.line(frame, (x1,y1), (x2,y2), (255,255,255), 2)
            cv.line(frame, (x2,y2), (x3,y3), (255,255,255), 2)
            cv.circle(frame, (x1, y1), 10, color, cv.FILLED)
            cv.circle(frame, (x1, y1), 15, color)

            # X2
            cv.circle(frame, (x2, y2), 10, color, cv.FILLED)
            cv.circle(frame, (x2, y2), 15, color)

            # X3
            cv.circle(frame, (x3, y3), 10, color, cv.FILLED)
            cv.circle(frame, (x3, y3), 15, color)

            # Display the angle
            cv.putText(frame, f"{int(angle)}", (x2+25,y2+10), cv.FONT_HERSHEY_PLAIN, 1, (255,0,0), 2)

        return angle