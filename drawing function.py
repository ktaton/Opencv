import numpy as np
import cv2

#img = cv2.imread('lena.jpg', 1)
img = np.zeros([512,512,3], np.uint8)

img = cv2.line(img, (0,0), (255,255), (0,0,255), 5)
img = cv2.arrowedLine(img, (0,255), (255,255), (0,0,155), 5)
img = cv2.rectangle(img, (384,0), (510,128), (50,123,230), -1)
img = cv2.circle(img, (447,63), 63, (140,50,100), -1)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,140,50), 10, cv2.LINE_8)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()