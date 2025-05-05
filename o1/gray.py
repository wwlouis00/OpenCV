
import cv2

image = cv2.imread("螺絲.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite( 'gray.jpg', gray )

cv2.imshow("A01.py", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
