import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
grayimage = cv.imread('starry_night.jpg', 0)
edge= cv.Canny(grayimage, 120, 200)
plt.subplot(121),plt.imshow(grayimage,'gray'),plt.title('grayscale')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edge,'gray'),plt.title('pencil_sketch')
plt.xticks([]), plt.yticks([])
plt.show()
