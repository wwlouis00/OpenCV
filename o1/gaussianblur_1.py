
import cv2

image = cv2.imread("Blur.jpg")

cv2.imwrite( 'Blur_7.jpg', cv2.GaussianBlur(image, (7, 7), 0) )

cv2.imwrite( 'Blur_17.jpg', cv2.GaussianBlur(image, (17, 17), 0) )

cv2.imwrite( 'Blur_21.jpg', cv2.GaussianBlur(image, (21, 21), 0) )
cv2.imwrite( 'Blur_23.jpg', cv2.GaussianBlur(image, (23, 23), 0) )
cv2.imwrite( 'Blur_25.jpg', cv2.GaussianBlur(image, (25, 25), 0) )

cv2.imwrite( 'Blur_29.jpg', cv2.GaussianBlur(image, (29, 29), 0) )

cv2.imwrite( 'Blur_37.jpg', cv2.GaussianBlur(image, (37, 37), 0) )

cv2.imwrite( 'Blur_45.jpg', cv2.GaussianBlur(image, (45,45), 0) )

cv2.imwrite( 'Blur_20.jpg', cv2.GaussianBlur(image, (20, 20), 0) )

