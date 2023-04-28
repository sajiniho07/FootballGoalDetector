import cv2
import numpy as np

class FootballGoalDetection():

    def __init__(self):
        self.sensitive_area_x1 = 190
        self.sensitive_area_y1 = 140
        self.sensitive_area_x2 = 520
        self.sensitive_area_y2 = 355
        self.m, self.b = self.get_gate_sens_line_m_b()
     
    def get_gate_sens_line_m_b(self):
        img = cv2.imread('res/2.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        ltl_edg = edges[self.sensitive_area_y1:self.sensitive_area_y2, self.sensitive_area_x1:self.sensitive_area_x2]
        lines = cv2.HoughLinesP(ltl_edg, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
        min_x = 0
        for line in lines:
            x1, y1, x2, y2 = line[0]
            m = abs((y2 - y1) / (x2 - x1))
            if 0.5 < m < 1 and min_x < x1:
                # point_1 = (self.sensitive_area_x1 + x1, self.sensitive_area_y1 + y1)
                # point_2 = (self.sensitive_area_x1 + x2, self.sensitive_area_y1 + y2)
                # cv2.line(img, point_1, point_2, (255, 0, 0), 1)
                min_x = x1
                b = -m * (self.sensitive_area_x1 + x1) + (self.sensitive_area_y1 + y1)
                return m, b
            
    def get_image_and_processed_edges(self, name):
        img = cv2.imread(f"res/{name}.jpg")
        height, width = img.shape[:2]
        new_size = (width*2, height*2)
        resized_img = cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7, 7), 3)
        edges = cv2.Canny(blur, 100, 200, apertureSize=3)
        ltl_edg = edges[self.sensitive_area_y1*2:self.sensitive_area_y2*2, self.sensitive_area_x1*2:self.sensitive_area_x2*2]
        return img, ltl_edg

    def is_goal_detected(self, x_cent, y_cent, radius):
        m, b = self.m, self.b
        yhat = x_cent * m + b
        if yhat > y_cent:
            return False
        else:
            distance = abs(m*x_cent-y_cent+b)/(m**2+1)**0.5
            return distance > radius

    def goal_detector(self):
        for i in range(1, 7):
            img, edges = self.get_image_and_processed_edges(i)
            circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=100, param1=1.8, param2=12, minRadius=10, maxRadius=15)
            if circles is not None:
                circle = circles[0].astype(np.uint32)[0]
                x_cent = self.sensitive_area_x1 + int(circle[0] / 2)
                y_cent = self.sensitive_area_y1 + int(circle[1] / 2)
                radius = int(circle[2] / 2)
                # cv2.circle(img, (x_cent, y_cent), radius, (0, 0, 255), 1)
                is_goal_detected = self.is_goal_detected(x_cent, y_cent, radius)
                if is_goal_detected:
                    print(f"Goal detected in frame name: {i}")
            # cv2.imshow("img", img)
            # cv2.waitKey(0)
        if not is_goal_detected:
            print(f"No Goal detected.")

football_goal_detection = FootballGoalDetection()
football_goal_detection.goal_detector()
