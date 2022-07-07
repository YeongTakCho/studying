import cv2 as cv

cap = cv.VideoCapture(0)
assert cap.isOpened()

classifier = cv.CascadeClassifier(
    'projects/detectNum/haarcascade_frontalface_default.xml')
assert not classifier.empty()

print('starting cam')
while(True):
    ret, cam = cap.read()

    if(ret):
        faces = classifier.detectMultiScale(cam)
        cv.rectangle(cam, faces, (255, 0, 255), 2)
        cv.imshow('camera', cam)
        if cv.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv.destroyAllWindows()
