import numpy as np
import cv2 as cv


def on_trackbar_change(value):
    print(value)


img = np.zeros((300,512,3), np.uint8)
cv.namedWindow("image")

cv.createTrackbar("B", "image", 0, 255, on_trackbar_change)
cv.createTrackbar("G", "image", 0, 255, on_trackbar_change)
cv.createTrackbar("R", "image", 0, 255, on_trackbar_change)

switch = "0 : OFF\n 1 : ON"
cv.createTrackbar(switch, "image", 0, 1, on_trackbar_change)


while(1):
    cv.imshow("image", img)
    k = cv.waitKey(1)
    if k == 27:
        break

    blue = cv.getTrackbarPos("B", "image")
    green = cv.getTrackbarPos("G", "image")
    red = cv.getTrackbarPos("R", "image")
    Switch = cv.getTrackbarPos( switch, "image")

    if Switch == 0:
        img[:] = 0
    else:
        img[:] = [blue, green, red]
cv.destroyAllWindows()