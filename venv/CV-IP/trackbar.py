import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('C:/Users/Admin/Pictures/tennis.jpg')
img[np.all(img < 169, axis=2)] = 0
img[np.all(img > 134, axis=2)] = 0

def nothing(x):
    print(x)
b, g, r = cv2.split(img)

_, threshold = cv2.threshold(g, 127, 255, cv2.THRESH_BINARY)

cv2.namedWindow('image')
cv2.createTrackbar('dilated', 'image', 0, 14, nothing)
cv2.createTrackbar('iteration', 'image', 0, 30, nothing)
while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    dilated = cv2.getTrackbarPos('dilated','image')
    ite = cv2.getTrackbarPos('iteration','image')
    dilate = cv2.dilate(threshold, (dilated, dilated), iterations=ite)
    cv2.imshow('image', dilate)