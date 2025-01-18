import cv2
import numpy as np
import matplotlib.pylab as plt

def roi(image, vertices):
    mask = np.zeros_like(image)
    #channel_count = image.shape[2]
    match_mask_color = (255)#*channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def draw_the_lines(image, lines):
    image = np.copy(image)
    line_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_image, (x1,y1), (x2,y2), (0,255,0), 3)

    image = cv2.addWeighted(image, 0.8, line_image, 1, 0.0)
    return image
#image = cv2.imread('road.jpg')
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def process(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]

    roi_vertices = [(0, height/1.2), (width/2, height/3), (width, height/1.3)]


    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(gray_image, 100, 150)
    cropped_image = roi(canny, np.array([roi_vertices], np.int32))
    lines = cv2.HoughLinesP(cropped_image, rho=6, theta=np.pi/180, threshold=40, lines=np.array([]), minLineLength=20, maxLineGap=60)

    image_with_lines = draw_the_lines(image, lines)
    return image_with_lines
cap = cv2.VideoCapture('road.avi.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord(('q')):
        break

cap.release()
cv2.destroyAllWindows()
