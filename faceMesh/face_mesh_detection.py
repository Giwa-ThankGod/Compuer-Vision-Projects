import time
import cv2 as cv
import face_mesh_module as fm

def main():
    cap = cv.VideoCapture('videos/face/vid2.mp4')
    pTime = 0
    detector = fm.FaceMeshDetector()
    while True:
        success, frame = cap.read()
        frame, face_landmarks = detector.drawMesh(frame)

        # if len(face_landmarks) > 0:
            # print(len(face_landmarks))  # display the number of faces detected.

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv.putText(frame, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)
        
        cv.imshow("Image", frame)

        if cv.waitKey(15) & 0xff==ord('q'):
            break


if __name__ == "__main__":
    main()