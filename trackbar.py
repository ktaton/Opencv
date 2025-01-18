import numpy as np
import cv2

def nothing(x):
    print(x)

#img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('CP', 'image', 10, 400, nothing)


switch = '0: OFF\n 1: ON\n'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv2.imread('lena.jpg')
    pos = cv2.getTrackbarPos('CP','image')
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, str(pos), (50,100), font, 3, (130,30,30))

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.imshow('image', img)

cv2.destroyAllWindows()