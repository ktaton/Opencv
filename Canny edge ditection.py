import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', 0)
canny = cv2.Canny(img, 100, 200)

titles = ['image', 'canny']
image = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(image[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()