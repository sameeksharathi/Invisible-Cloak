import cv2

#This is a webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # background is what the camera is reading
    ret, background = cap.read()  # Here is am simply reading file
    if ret:
        cv2.imshow("image", background)
        if cv2.waitKey(5) == ord("q"):
            # save the image
            cv2.imwrite('./image.jpg', background)
            break

cap.release()
cv2.destroyAllWindows()