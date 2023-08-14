import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("data/water.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

karnel = np.ones((5, 5), np.float32)/25

##filter types
dst = cv2.filter2D(img, -1, karnel)
blur = cv2.blur(img, (5,5))
gaussianBlur = cv2.GaussianBlur(img, (5, 5), 0)
medianBlur = cv2.medianBlur(img, 5) ## best
bilateralFilter = cv2.bilateralFilter(img, 9, 75,75)

titles = ["image", "2D Convolution", "blur", "gaussianBlur", "medianBlur", "bilateralFilter"]
images = [img, dst, blur, gaussianBlur, medianBlur, bilateralFilter]

for i in range(6):
    plt.subplot(3, 3, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()