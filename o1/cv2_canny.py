# python cv2_canny.py -i t02.jpg
# python cv2_canny.py -i t00b.jpg
import argparse
import imutils
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="path to input image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (11, 11), 0)

cv2.imshow("canny10-30", cv2.Canny(gray,10, 30  ))
cv2.imshow("canny80",   cv2.Canny(gray,80, 110  ))
cv2.imshow("canny30",   cv2.Canny(gray,30, 110  ))
cv2.imshow("canny50-220",   cv2.Canny(gray,50, 220  ))

cv2.imshow("gray", gray  )
cv2.waitKey(0)
cv2.destroyAllWindows()

