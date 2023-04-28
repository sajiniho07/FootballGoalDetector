import cv2
from ultralytics import YOLO

model = YOLO("models/yolov8n")
results = model.predict(source=0, show=True)

