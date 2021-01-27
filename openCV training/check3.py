import cv2
import numpy as np 
import matplotlib.pyplot as plt
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

image = cv2.imread("starry_night.jpg")
image= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image)

pixel_values = image.reshape((-1,3))
pixel_values = np.float32(pixel_values)

#define stopping criteria,0.85 refers to epsilon which is when accuracy becomes 85%
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)

k=3
retval, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS) 
centers = np.uint8(centers)
segmented_data = centers[labels.flatten()] # falatten to 1-D matrix
segmented_image = segmented_data.reshape((image.shape))
plt.imshow(segmented_image)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

