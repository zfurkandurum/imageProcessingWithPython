import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
The Canny edge detection algorithm is composed of 5 steps:

1. Noise reduction

2. Gradient calculation

3. Non-maximum suppression

4. Double threshold

5. Edge Tracking by Hysteresis

"""
img = cv2.imread("data/messi5.jpg", 0)
canny = cv2.Canny(img, 100, 200)

titles = ["image", "canny"]
images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()