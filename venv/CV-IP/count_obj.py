import cv2
import matplotlib.pyplot as plt
import numpy as np

def hatgao1():
    img = cv2.imread('C:/Users/Admin/Pictures/Images_Proj1_topic1/hatgao1.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #erode = cv2.erode(gray, (1, 1), iterations=3)
    #blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, threshold = cv2.threshold(gray, 113, 255, cv2.THRESH_BINARY)
    #threshold = np.uint8(threshold)
    distance = cv2.distanceTransform(threshold, cv2.DIST_L2, 3)
    normalize = cv2.normalize(distance, 0, 1.0, cv2.NORM_MINMAX)
    _, threshold2 = cv2.threshold(normalize, 0.005, 1.0, cv2.THRESH_BINARY)
    kernel1 = np.ones((3,3), dtype=np.uint8)
    dist = cv2.dilate(threshold2, kernel1)
    dist_8u = dist.astype('uint8')
    cnt, hierarchy = cv2.findContours(dist_8u, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
    plt.imshow(rgb, cmap='gray')
    plt.show()
    print(len(cnt))

def hatgao2():
    img = cv2.imread('C:/Users/Admin/Pictures/Images_Proj1_topic1/hatgao2.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 3)
    _, threshold = cv2.threshold(blur, 113, 255, cv2.THRESH_BINARY)
    #threshold = np.uint8(threshold)
    distance = cv2.distanceTransform(threshold, cv2.DIST_L2, 3)
    normalize = cv2.normalize(distance, 0, 1.0, cv2.NORM_MINMAX)
    _, threshold2 = cv2.threshold(normalize, 0.005, 1.0, cv2.THRESH_BINARY)
    kernel1 = np.ones((3,3), dtype=np.uint8)
    dist = cv2.dilate(threshold2, kernel1)
    dist_8u = dist.astype('uint8')
    cnt, hierarchy = cv2.findContours(dist_8u, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
    plt.imshow(rgb, cmap='gray')
    plt.show()
    print(len(cnt))

def hatgao3():
    img = cv2.imread('C:/Users/Admin/Pictures/Images_Proj1_topic1/hatgao3.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 5)
    blur = cv2.GaussianBlur(threshold, (9, 9), 0)
    #blur = cv2.medianBlur(threshold, 1)

    canny = cv2.Canny(blur, 1,250)
    kernel1 = np.ones((3,3), dtype=np.uint8)
    dist = cv2.dilate(canny, kernel1)
    dist_8u = dist.astype('uint8')
    cnt, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 3)

    titles = ['Img', 'Gray', 'Threshold', 'Blur', 'Canny', 'RGB']
    images = [img, gray, threshold, blur, canny, rgb]

    for i in range(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
    print(len(cnt))

def hatgao4():
    img = cv2.imread('C:/Users/Admin/Pictures/Images_Proj1_topic1/hatgao4.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #blur = cv2.medianBlur(gray, 3)
    _, threshold = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    #threshold = np.uint8(threshold)
    distance = cv2.distanceTransform(threshold, cv2.DIST_L2, 3)
    normalize = cv2.normalize(distance, 0, 1.0, cv2.NORM_MINMAX)
    _, threshold2 = cv2.threshold(normalize, 0.005, 1.0, cv2.THRESH_BINARY)
    kernel1 = np.ones((3,3), dtype=np.uint8)
    dist = cv2.dilate(threshold2, kernel1)
    dist_8u = dist.astype('uint8')
    cnt, hierarchy = cv2.findContours(dist_8u, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
    plt.imshow(rgb, cmap='gray')
    plt.show()
    print(len(cnt))

hatgao3()