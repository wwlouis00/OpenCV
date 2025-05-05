import cv2

image = cv2.imread("gray.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("thresh110", cv2.threshold(gray,110, 255, cv2.THRESH_BINARY_INV)[1]  )
cv2.imshow("thresh80",   cv2.threshold(gray,80, 255, cv2.THRESH_BINARY_INV)[1]  )
cv2.imshow("thresh75",   cv2.threshold(gray,75, 255, cv2.THRESH_BINARY_INV)[1]  )
cv2.imshow("thresh70",   cv2.threshold(gray,70, 255, cv2.THRESH_BINARY_INV)[1]  )
cv2.imshow("thresh30",   cv2.threshold(gray,30, 255, cv2.THRESH_BINARY_INV)[1]  )

cv2.waitKey(0)
cv2.destroyAllWindows()
