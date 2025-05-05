
import cv2

image = cv2.imread("Blur.jpg")

blurred = cv2.GaussianBlur(image, (11, 11), 0)

cv2.imwrite( 'Blur_11.jpg', blurred )


