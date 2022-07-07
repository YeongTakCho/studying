import cv2 as cv
from time import sleep

restoreDir = 'projects/detectNum/images/one'
cap = cv.VideoCapture(0)
for i in range(100):
    sleep(0.2)
    ret, cam = cap.read()

    if(ret):
        cv.imshow('camera', cam)
        cv.imwrite(restoreDir + '/' + str(i) + '.jpg', cam)
        print('restore img ' + str(i) + '.jpg')
        if cv.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv.destroyAllWindows()
