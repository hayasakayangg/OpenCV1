import cv2
import matplotlib.pyplot as plt
import numpy as np

def hatgao1():
    img = cv2.imread("C:/Users/Admin/Pictures/Images_Proj1_topic1/hatgao1.png", cv2.IMREAD_GRAYSCALE)
    # Dùng adaptive threshold
    threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, -20)
    #cv2.imshow("Adaptive Thresholding", threshold)

    # Thu nhỏ hạt gạo
    kernel = np.ones((3, 3), np.uint8)
    erode = cv2.erode(threshold, kernel)
    #cv2.imshow("Morphological Erosion", output_erosion)

    # Find contour
    contours, _ = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output_contour = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(output_contour, contours, -1, (0, 0, 255), 2)
    print("Số hạt gạo: ", len(contours))
    #cv2.imshow("Contours", output_contour)

    titles = ['Ảnh gốc', 'Threshold', 'Thu nhỏ', 'Kết quả']
    images = [img, threshold, erode, output_contour]

    for i in range(4):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

def hatgao2():
    img = cv2.imread('C:/Users/Admin/Pictures/Images_Proj1_topic1/hatgao2.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #
    blur = cv2.medianBlur(gray, 3)
    #
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(blur, kernel, iterations=1)
    #
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(erosion, cv2.MORPH_GRADIENT, kernel)
    #
    equ = cv2.equalizeHist(opening)
    #
    _, thresh = cv2.threshold(equ, 221, 255, 0)
    #
    cnt, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ct = []
    for contour in cnt:
        if cv2.contourArea(contour) > 0:
            ct.append(cv2.contourArea(contour))
            cv2.drawContours(rgb, contour, -1, (0, 255, 0), 3)
    print('Số hạt gạo đếm được:', len(ct))
    titles = ['Ảnh xám', 'Median Blur', 'Erosion', 'Morphology', 'Cân bằng sáng', 'Threshold', 'Kết quả']
    images = [gray, blur, erosion, opening, equ, thresh, rgb]
    for i in range(7):
        plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

def hatgao3():
    ic = cv2.imread('C:/Users/Admin/Pictures/Images_Proj1_topic1/hatgao3.png', 0)
    ic = cv2.resize(ic, (500, 500))
    #
    img = np.zeros((500, 500))
    # y=a*sin(2*pi*f*t)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            img[y, x] = 255 * (np.sin(np.pi * 8 * (1 / img.shape[1]) * (x + 10)))
    #
    img = np.abs(img).astype(np.uint8)
    #
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    m = 20 * np.log(np.abs(fshift))
    #
    f2 = np.fft.fft2(ic)
    fshift2 = np.fft.fftshift(f2)
    m2 = 20 * np.log(np.abs(fshift2))
    #
    rows, cols = img.shape
    crow, ccol = rows // 2, cols // 2
    fshift2[fshift != 0] = 0
    f_ishift2 = np.fft.ifftshift(fshift2)
    img_back = np.fft.ifft2(f_ishift2)
    img_back = np.real(img_back)
    #
    res = np.zeros(img_back.shape)
    res = cv2.normalize(img_back, res, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    #
    res2 = np.zeros((499, 499), dtype=int)
    for i in range(499):
        for j in range(499):
            res2[i][j] = res[i][j]
    res2 = np.uint8(res2)
    #
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(res2, kernel, iterations=1)
    #
    blur = cv2.medianBlur(erosion, 5)
    #
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(blur, cv2.MORPH_GRADIENT, kernel)
    #
    equ = cv2.equalizeHist(opening)
    #
    _, thresh = cv2.threshold(equ, 221, 255, 0)
    #
    cnt, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(ic, cv2.COLOR_BGR2RGB)
    ct = []
    for contour in cnt:
        if cv2.contourArea(contour) > 0:
            ct.append(cv2.contourArea(contour))
            cv2.drawContours(rgb, contour, -1, (255, 0, 0), 3)
    print("Số hạt gạo: ", len(ct))

    titles = ['IMG Back', 'Blur', 'Morphology', 'EqualizeHist', 'Threshold', 'Kết quả']
    images = [res2, blur, opening, equ, thresh, rgb]

    for i in range(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

def hatgao4():
    img = cv2.imread('C:/Users/Admin/Pictures/Images_Proj1_topic1/hatgao4.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    threshold = np.uint8(threshold)


    # Find contour
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output_contour = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(output_contour, contours, -1, (0, 0, 255), 2)
    print("Số hạt gạo: ", len(contours))
    # cv2.imshow("Contours", output_contour)

    titles = ['Ảnh gốc', 'Threshold', 'Kết quả']
    images = [img, threshold, output_contour]

    for i in range(3):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

hatgao4()