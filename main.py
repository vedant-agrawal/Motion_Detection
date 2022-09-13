# Importing dependencies
import cv2

capture = cv2.VideoCapture('vtest.avi')

# Showing the original video
while capture.isOpened():
    _, frame = capture.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(50) == 27:
        break

cv2.destroyAllWindows()


_, frame1 = capture.read()
_, frame2 = capture.read()

while capture.isOpened():
    # Getting abs difference between consecutive frames
    difference = cv2.absdiff(frame1, frame2)
    # Converting the difference to grayscale
    grayScale = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    # Applying GaussianBlur to the grayscale difference
    blurred = cv2.GaussianBlur(grayScale, (5, 5), 0)
    # Applying binary threshing to the blurred image
    _, threshed = cv2.threshold(blurred, 20, 255, cv2.THRESH_BINARY)
    # Dilating
    dilated = cv2.dilate(threshed, None, iterations=2)
    # Finding contours and applying boundingRectangle to the contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 800:
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imshow("Video", frame1)
    frame1 = frame2
    _, frame2 = capture.read()
    if cv2.waitKey(50) == 27:
        break

cv2.destroyAllWindows()
capture.release()
