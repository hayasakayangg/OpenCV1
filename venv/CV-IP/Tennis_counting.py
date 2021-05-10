import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('C:/Users/Admin/Pictures/tennis.jpg')
img3 = img.copy()
img[np.all(img < 169, axis=2)] = 0
img[np.all(img > 134, axis=2)] = 0

def nothing(x):
    print(x)
b, g, r = cv2.split(img)

_, threshold = cv2.threshold(g, 127, 255, cv2.THRESH_BINARY)

dilated = cv2.dilate(threshold, (7, 7), iterations=29)

distance = cv2.distanceTransform(dilated, cv2.DIST_L2, 3)

normalize = cv2.normalize(distance, 0, 1.0, cv2.NORM_MINMAX)

_, threshold2 = cv2.threshold(normalize, 5/2000, 1, cv2.THRESH_BINARY)

kernel1 = np.ones((3,3), dtype=np.uint8)
dist = cv2.dilate(threshold2, kernel1)
dist_8u = dist.astype('uint8')

cnt, hierarchy = cv2.findContours(dist_8u, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (255, 0, 255), 2)
plt.imshow(rgb, cmap = 'gray')
plt.show()
print(len(cnt))