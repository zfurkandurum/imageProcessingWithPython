import cv2
import numpy as np

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ', y)
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 1, (255,255,0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0,255,255), 2)
        cv2.imshow('image', img)


img = cv2.imread("data/aloeR.jpg")
cv2.imshow('image', img)

cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()