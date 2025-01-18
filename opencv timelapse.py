import cv2

cap = cv2.VideoCapture(0)
x = 0
while(True):
    ret, frame = cap.read()
    file_path = 'saved_media/''image'+str(x)+'.jpg'
    x += 1
    cv2.imwrite(file_path, frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()