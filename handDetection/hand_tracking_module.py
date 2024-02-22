import time
import cv2 as cv
import mediapipe as np

class handDetector():
    """
    This helps us access the landmarks of hands available on an image.
    """

    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.npHands = np.solutions.hands
        self.hands = self.npHands.Hands()
        self.npDraw = np.solutions.drawing_utils

    def findHands(self, frame, draw=True):
        # resizing frame for better view
        frame = cv.resize(frame, (800,600))

        frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        self.results = self.hands.process(frameRGB)
        
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.npDraw.draw_landmarks(frame, handLms, self.npHands.HAND_CONNECTIONS)
                else:
                    break

        return frame

    def findPosition(self, frame, handNo=0, draw=True):

        lmlist = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
        
                h, w, c = frame.shape #Get the height, width and channel of the frame.
                
                cx, cy = int(lm.x*w), int(lm.y*h) #To get the pixel values.

                lmlist.append([id, cx, cy])

                if draw:
                    cv.circle(
                        frame, 
                        (cx, cy), #Position to draw on.
                        5, #Radius.
                        (0, 255, 0), #Color
                        cv.FILLED
                    )

        return lmlist