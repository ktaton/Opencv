import cv2
import numpy as np

cap = cv2.VideoCapture('traffic3.mp4')
a = 0
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

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while True:

    frame01 = process(frame1)
    frame02 = process(frame2)

    diff = cv2.absdiff(frame01, frame02)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=2)
    contours,_ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1, contours, -1, (0,255,0), 2)

    counter1 = 0

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 400:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0, 255, 0), 2)

        #cv2.putText(frame1, "status: {}".format('Movement'), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        #cv2.putText(frame1, "No: {}".format(), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)


    cv2.imshow('feed', frame1)
    cv2.imshow('fg', frame01)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()