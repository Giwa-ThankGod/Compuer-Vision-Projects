import cv2 as cv

img = cv.imread(r'cv1/photos/face1.jpg')
# cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# print(gray.shape)
# print(cv.samples.findFile(r"haarcascade_frontalface_default.xml"))
haar_cascade = cv.CascadeClassifier(cv.samples.findFile(r"cv1\haar_cascade\haarcascade_frontalface_default.xml"))

# print(haar_cascade.empty())
# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=5)

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

# Printing the value of faces_rect causes the window to lag :: avoid uncommenting this line
# print(faces_rect)

print(f'Number of faces found = {len(faces_rect)}')
# cv.imshow('Face Detection', faces_rect)

for (x,y,w,h) in faces_rect:
    cv.rectangle(
        img,
        (x, y),
        (x+w, y+h),
        (0,255,0),
        2 
        )
    
cv.imshow('Detected Faces', img)
cv.imwrite('cv1/photos/detectedFaces3.jpg', img)

cv.waitKey(0)
cv.destroyAllWindows()