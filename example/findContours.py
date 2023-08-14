import cv2
import numpy as np

img = cv2.imread("data/opencv-logo2.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgGray, 127, 255, 0)
contours, hieracvhy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("number of contours = " + str(len(contours)))
print(contours[0])

cv2.drawContours(img, contours, -10, (0,255,0), 3)

cv2.imshow("image", img)
cv2.imshow("imgGray", imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()