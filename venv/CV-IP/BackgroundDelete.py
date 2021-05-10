import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('C:/Users/Admin/Pictures/tennis.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (7, 7), 0)

canny = cv2.Canny(blur, 1, 100, 3)

# difference = cv2.absdiff(img, blur)
# difference = np.sum(difference, axis=2)/4.0

# _,threshold = cv2.threshold(difference, 0.5, 255, cv2.THRESH_BINARY)
# threshold = np.uint8(threshold)

# distance = cv2.distanceTransform(threshold, cv2.DIST_L2, 3)
kernel1 = np.ones((3,3), dtype=np.uint8)
dist = cv2.dilate(canny, kernel1)
dist_8u = dist.astype('uint8')

cnt, hierarchy = cv2.findContours(dist_8u, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (255, 0, 255), 2)
print(len(cnt))
titles = ['original', 'Gray', 'Gaussian', 'Canny', 'RGB']
images = [img, gray, blur, canny, rgb]
for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()