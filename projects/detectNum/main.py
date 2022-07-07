import cv2 as cv

cap = cv.VideoCapture(0)
assert cap.isOpened()
frame_width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)

classifier = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
assert not classifier.empty()

print('starting cam')

while(True):
    ret, cam = cap.read()
    if(ret):
        faces = classifier.detectMultiScale(cam)
        for (x, y, w, h) in faces:
            cv.rectangle(cam, (x, 0, w, int(frame_height)), (0, 0, 0), -1)
        cv.imshow('camera', cam)

        if cv.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv.destroyAllWindows()
