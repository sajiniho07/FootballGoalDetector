import cv2
from ultralytics import YOLO
import numpy as np

class FootballGoalDetection():

    def __init__(self):
        self.sensitive_area_x1 = 190
        self.sensitive_area_y1 = 140
        self.sensitive_area_x2 = 520
        self.sensitive_area_y2 = 355
        self.m, self.b = self.get_gate_sens_line_m_b()
        self.model = YOLO("models/yolov8x")
     
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
                min_x = x1
                b = -m * (self.sensitive_area_x1 + x1) + (self.sensitive_area_y1 + y1)
                return m, b
            
    def is_goal_detected(self, x_cent, y_cent, radius):
        m, b = self.m, self.b
        yhat = x_cent * m + b
        if yhat > y_cent:
            return False
        else:
            distance = abs(m*x_cent-y_cent+b)/(m**2+1)**0.5
            return distance > radius

    def goal_detector(self):
        is_goal_detected = False
        for i in range(1, 7):
            img = cv2.imread(f"res/{i}.jpg")
            results = self.model.predict(source=img)
            for result in results:
                for (obj_xyxy, obj_cls) in zip(result.boxes.xyxy, result.boxes.cls):
                    obj_cls = int(obj_cls)
                    x1 = obj_xyxy[0].item()
                    y1 = obj_xyxy[1].item()
                    x2 = obj_xyxy[2].item()
                    y2 = obj_xyxy[3].item()
                    # cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 1)
                    if obj_cls == 32:
                        x_cent = (x2+x1)/2
                        y_cent = (y2+y1)/2
                        radius = ((x2-x1)/2+(y2-y1)/2)/2
                        is_goal_detected = self.is_goal_detected(x_cent, y_cent, radius)
                        if is_goal_detected:
                            print(f"Goal detected in frame name: {i}")

            # cv2.imshow("img", img)
            # cv2.waitKey(0)

        if not is_goal_detected:
            print(f"No Goal detected.")

football_goal_detection = FootballGoalDetection()
football_goal_detection.goal_detector()
