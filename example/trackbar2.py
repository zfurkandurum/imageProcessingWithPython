import cv2
import numpy as np
import cv2 as cv


def on_trackbar_change(value):
    print(value)

cv.namedWindow("image")

cv.createTrackbar("CP", "image", 10, 400, on_trackbar_change)

switch = "color/gray"
cv.createTrackbar(switch, "image", 0, 1, on_trackbar_change)

while(1):
    img = cv.imread("data/lena.jpg")
    position = cv.getTrackbarPos("CP", "image")
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv.putText(img,str(position), (50, 150), font, 4, (0,0,255))
    k = cv.waitKey(1)
    if k == 27:
        break

    Switch = cv.getTrackbarPos( switch, "image")

    if Switch == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow("image", img)

cv.destroyAllWindows()