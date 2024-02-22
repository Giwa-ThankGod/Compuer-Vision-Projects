import time

import cv2 as cv
import mediapipe as np

capture = cv.VideoCapture(0)

npHands = np.solutions.hands
hands = npHands.Hands()
npDraw = np.solutions.drawing_utils

pTime = 0
cTime = 0

while capture.isOpened():
    # capture frame by frame
    success, frame = capture.read()

    # resizing frame for better view
    frame = cv.resize(frame, (800,600))

    frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    results = hands.process(frameRGB)
    # print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            # print(handLms)
            # landmark {
            #     x: 0.493496835231781
            #     y: 0.7553028464317322
            #     z: 2.159129479650801e-07
            # }

            # print(handLms.landmark)
            # [
            #     x: 0.493496835231781
            #     y: 0.7553028464317322
            #     z: 2.159129479650801e-07
            #     , x: 0.448952317237854
            #     y: 0.7278738021850586
            #     z: -0.01812795363366604
            # ]

            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                # 0 x: 0.493496835231781
                # y: 0.7553028464317322
                # z: 2.159129479650801e-07

                # 1 x: 0.448952317237854
                # y: 0.7278738021850586
                # z: -0.01812795363366604

                h, w, c = frame.shape #Get the height, width and channel of the frame :: line 20.
                
                cx, cy = int(lm.x*w), int(lm.y*h) #To get the pixel values.

                # print(id, cx, cy)

                if id == 0:
                    cv.circle(
                        frame, 
                        (cx, cy), #Position to draw on.
                        25, #Radius.
                        (255, 0, 255), #Color
                        cv.FILLED
                    )

            npDraw.draw_landmarks(frame, handLms, npHands.HAND_CONNECTIONS)

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
