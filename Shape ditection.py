import cv2
import numpy as np

img = cv2.imread('Shapes.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0,255,0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[0]

    if len(approx) == 3:
       cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
    elif len(approx) == 4:
       x, y, w, h = cv2.boundingRect(approx)
       aspectRatio = float(w)/h
       print(aspectRatio)
       if aspectRatio >= 0.95 and aspectRatio <=1.05:
         cv2.putText(img, "Square", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
       else:
         cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
    elif len(approx) == 5:
       cv2.putText(img, "Pentagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
    elif len(approx) == 10:
       cv2.putText(img, "Star", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
    else :
       cv2.putText(img, "Circle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
