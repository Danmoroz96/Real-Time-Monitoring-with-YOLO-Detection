import cv2
from ultralytics import YOLO

STREAM_URL = "http://127.0.0.1:5000/video_feed"

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(STREAM_URL)

if not cap.isOpened():
    print("Error: Could not open stream.")
    exit()

print("Stream opened. Running YOLO detection...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Home Monitoring", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()