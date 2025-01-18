import cv2
import numpy as np

cap = cv2.VideoCapture('traffic3.mp4')

#kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernal)

    #cv2.imshow('Frame', frame)
    cv2.imshow('Fg mask frame', fgmask)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()