import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('traffic3.mp4')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

counterL = 0
counterR = 0

def roi(image, vertices):
    mask = np.zeros_like(image)
    #channel_count = image.shape[2]
    match_mask_color = (255)#*channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def process(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    vertices = np.array([[0,480], [20,300], [300,200], [600,120], [800,260], [840,480]], np.int32)
    image = roi(image, [vertices])
    return image

while True:
    ret, frame = cap.read()
    frame1 = process(frame)
    if frame1 is None:
        break
    fgmask = fgbg.apply(frame1)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernal)
    _, thresh = cv2.threshold(fgmask, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours,_ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    counter = 0

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 500:
            continue

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if x < 420 and y > 330 and y < 334:
            counterL +=1
        if x > 430 and  y> 330 and y < 337:
            counterR +=1
        cv2.putText(frame, "Outgoing: {}".format(counterL), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 150, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "Incoming: {}".format(counterR), (620, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 150), 2, cv2.LINE_AA)
        cv2.putText(frame, "Total: {}".format(counterL + counterR), (365, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Frame', dilated)
    cv2.imshow('Fg', frame)
    #plt.imshow('image', frame)

    if cv2.waitKey(3) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()