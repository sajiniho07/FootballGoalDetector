import cv2
from ultralytics import YOLO

model = YOLO("models/yolov8x")
results = model.predict(source=0, show=True)

