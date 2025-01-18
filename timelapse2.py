import cv2

for i in range(0, 76, 1):
   file_path = 'saved_media/''image' + str(i) + '.jpg'
   img = cv2.imread(file_path)
   cv2.imshow('fr', img)
   if cv2.waitKey(10) & 0xFF == 27:
       break
cv2.destroyAllWindows()