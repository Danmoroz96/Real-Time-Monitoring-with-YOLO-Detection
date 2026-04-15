import cv2
from ultralytics import YOLO

# Remember to use localhost since it's all on one machine
STREAM_URL = "http://127.0.0.1:5000/video_feed"

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(STREAM_URL)

if not cap.isOpened():
    print("Error: Could not open stream.")
    exit()

print("Stream opened. Running YOLO detection...")

# Counter for our saved images
person_count = 1 

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Run YOLO detection on the frame
    results = model(frame)
    annotated_frame = results[0].plot()

    # We will use this flag to decide if we should save the image
    person_detected = False

    print("--- New Frame ---")
    
    # Extract data from the results
    for result in results:
        for box in result.boxes:
            # 1. Get the class ID (a number)
            class_id = int(box.cls[0])
            
            # 2. Translate the ID to a name (e.g., 'person', 'cup')
            class_name = model.names[class_id]
            
            # --- OPTIONAL EXTENSION: Print the name ---
            print(f"Detected: {class_name}")

            # --- BONUS TASK: Check if it's a person ---
            if class_name == "person":
                person_detected = True

    # If a person was found in this frame, save the image
    if person_detected:
        # Format the filename with a leading zero (e.g., 01, 02)
        filename = f"person_detected_{person_count:02d}.jpg"
        
        # Save the annotated frame (with boxes) to your folder
        cv2.imwrite(filename, annotated_frame) 
        print(f"*** ALERT: Person saved to {filename} ***")
        
        person_count += 1

    # Display the live stream
    cv2.imshow("YOLO Home Monitoring", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
