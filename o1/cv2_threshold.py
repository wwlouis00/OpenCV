# python cv2_threshold.py -i t02.jpg
# python cv2_threshold.py -i t00b.jpg
import argparse
import imutils
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="path to input image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("thresh110", cv2.threshold(gray,110, 255, cv2.THRESH_BINARY)[1]  )
cv2.imshow("thresh80",   cv2.threshold(gray,80, 255,   cv2.THRESH_BINARY)[1]  )
cv2.imshow("thresh80-110",   cv2.threshold(gray,80, 110,   cv2.THRESH_BINARY)[1]  )
cv2.imshow("thresh50",   cv2.threshold(gray,50, 255,   cv2.THRESH_BINARY)[1]  )
cv2.imshow("thresh30",   cv2.threshold(gray,30, 255,   cv2.THRESH_BINARY)[1]  )

cv2.imshow("gray", gray  )
cv2.waitKey(0)
cv2.destroyAllWindows()

