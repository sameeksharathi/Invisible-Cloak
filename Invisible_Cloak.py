import numpy as np
import cv2

cap = cv2.VideoCapture(0)
background = cv2.imread('./image.jpg')

while cap.isOpened():
    # take each frame
    ret, frame = cap.read()
    if ret:
        # how do we convert rgb to hsv (hue saturation value)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2. imshow("hsv", hsv)
        
        # how to get hsv value?
        # lower: hue-10, 100, 100,   higher; hue+10, 255, 255
        red = np.uint8([[[0, 0, 255]]])                         # bgr format
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        # get hav value of red from bgr
        # print(hsv_red)

        # threshold the hsv value to get only red color

        l_red = np.array([0, 100, 100])
        u_red = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, l_red, u_red)
        # cv2.imshow('mask', mask)                # Red color will get highlighted and get a B/W picture where red is heighlighted by white
        
        # apply morphological Transformations for removing edges of that red cloth.
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=1)
        mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)

        # part1 is all things red replaced by background
        part1 = cv2.bitwise_and(background, background, mask=mask)
        #cv2.imshow('part1', part1)

        mask = cv2.bitwise_not(mask)

        # part2 is all things not red replaced by background
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow("part2", part2)

        cv2.imshow("cloak", part1 + part2)

        

        if cv2.waitKey(5) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
