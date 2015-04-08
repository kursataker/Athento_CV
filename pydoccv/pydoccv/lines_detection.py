import cv2
import numpy as np

#img = cv2.imread("../resources/lines.jpg")
img = cv2.imread("../resources/lines2.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

rho = 1
theta = np.pi/180
threshold = 200
minLineLength = 1000
maxLineGap = 100
lines = cv2.HoughLinesP(edges, rho, theta, threshold, minLineLength, maxLineGap)
counter = 0
for x1,y1,x2,y2 in lines[0]:
    counter += 1
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

print "There are {0} lines".format(counter)

cv2.imshow('houghlines.jpg',img)
cv2.waitKey()