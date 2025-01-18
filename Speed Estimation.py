import cv2
import numpy as np
import math
import matplotlib as plt

cap = cv2.VideoCapture('traffic3.mp4')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

def roi(image, vertices):
    mask = np.zeros_like(image)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def process(image):
    #print(image.shape)
    vertices = np.array([[0,480], [20,300], [300,200], [600,120], [800,260], [840,480]], np.int32)
    image = roi(image, [vertices])
    return image

x2 = 0
y2 = 0
a = 0
b = 0
i = 0
while True:
    ret, frame = cap.read()
    frame1 = process(frame)
    if frame1 is None:
        break
    fgmask = fgbg.apply(frame1)
    _, thresh = cv2.threshold(fgmask, 20 , 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours,_ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        coordinates = 'x'+str(i), 'y'+str(i), 'w'+str(i), 'h'+str(i)
        coordinates = cv2.boundingRect(contour)
        i += 1

        if cv2.contourArea(contour) < 500:
            continue
        a = 'x'+str(i)
        b = 'y'+str(i)
        c = 'x'+str(i-1)
        d = 'x'+str(i-1)
        cv2.rectangle(frame, ('x'+str(i), 'y'+str(i)), ('x'+str(i)+'w'+str(i), 'y'+str(i)+'h'+str(i)), (0, 255, 0), 2)
        if x2 == 0 and y2 == 0:
            break
        d = math.sqrt((a-c)**2)
        print(d, a, b)
        speed = d*0.2
        cv2.putText(frame, "S: {}".format(int(speed)), (a, b-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.line(frame, (a, b), (x2, y2), (0,0,255))
    x2 = a
    y2 = b

    cv2.imshow('fg', dilated)
    cv2.imshow('frame', frame)

    if cv2.waitKey(3) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
