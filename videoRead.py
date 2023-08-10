import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    
    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video', gray)
    
    if cv2.waitKey(1) == ord("q"):
       break

cap.release
cv2.destroyAllWindows