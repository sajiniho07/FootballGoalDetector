import cv2
import numpy as np

img = cv2.imread('res/2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

ltl_edg = edges[140:355, 190:520]
# cv2.imshow('Processed Image', edges)
# cv2.waitKey(0)
# quit()
lines = cv2.HoughLinesP(ltl_edg, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
# Draw lines on the image
min_x = 0
for line in lines:
    x1, y1, x2, y2 = line[0]
    m = abs((y2 - y1) / (x2 - x1))
    if 0.5 < m < 1 and min_x < x1:
        min_x = x1
        cv2.line(img, (190 + x1, 140 + y1), (190 + x2, 140 + y2), (255, 0, 0), 1)
        print(f"m = {m}")

# print(f"Detected Circles Count: {lines.__len__()}")
cv2.imshow('Processed Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# بارگیری تصویر
# img = cv2.imread('res/1.jpg')

# lower_range = np.array([0, 0, 0])
# upper_range = np.array([100, 100, 100])
# mask = cv2.inRange(img, lower_range, upper_range)

# img[mask > 0] = (255, 255, 255)

# # lower_range = np.array([40, 40, 40])
# # upper_range = np.array([180, 180, 180])
# # mask = cv2.inRange(img, lower_range, upper_range)

# # img[mask > 0] = (0, 0, 255)

# cv2.imshow('Processed Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()