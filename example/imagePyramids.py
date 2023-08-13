import cv2
import numpy as np
"""
1-Gaussian pyramid
2-Laplacian pyramid
"""
img = cv2.imread("data/lena.jpg")
layer = img.copy()
gaussianPyramid = [layer]


"""
lowerResolution1 = cv2.pyrDown(img)
lowerResolution2 = cv2.pyrDown(lowerResolution1)
higherResolution1 = cv2.pyrUp(lowerResolution2) 
"""
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussianPyramid.append(layer)
    cv2.imshow(str(i), layer)

layer = gaussianPyramid[5]
cv2.imshow("upper level Gaussian Pyramid", layer)
laplacianPyramid = [layer]

for i in range(5, 0 , -1):
    gaussian_extended = cv2.pyrUp(gaussianPyramid[i])
    laplacian = cv2.subtract(gaussianPyramid[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)



cv2.imshow("original image", img)
"""
cv2.imshow("pyrdown 1 image", lowerResolution1)
cv2.imshow("pyrdown 2 image", lowerResolution2)
cv2.imshow("pyrUp 2 image", higherResolution1)
"""

cv2.waitKey(0)
cv2.destroyAllWindows()