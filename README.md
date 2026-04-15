# Intelligent Home Monitoring System

This repository contains the code for a real-time IoT video monitoring system that streams webcam footage and performs object detection using YOLOv8. 

## System Setup (Laptop A & Laptop B)
For this lab, **both Laptop A (the Camera Node) and Laptop B (the AI Monitoring Node) were simulated on a single laptop**. 
* The laptop acted as the sender by capturing the webcam feed and hosting it via a Flask server.
* Simultaneously, the same laptop acted as the receiver by running a secondary script that fetched the local stream and applied YOLO object detection.

## Network Configuration
* **Sender IP Address:** `127.0.0.1` (Localhost)
* **Port:** `5000`
* **Stream URL:** `http://127.0.0.1:5000/video_feed`

## Execution Steps

### 1. How the Stream was Started
To initiate the camera node, a terminal was opened and the following command was executed:
`python app.py`
This started the Flask web server, turned on the laptop's webcam, and began continuously encoding and serving the frames as a multipart JPEG stream over the local network.

### 2. How YOLO was Run
While the Flask server was actively running, a **second terminal window** was opened to act as the AI node. The following command was executed:
`python yolo_stream.py`
This script used OpenCV to connect to the Flask stream URL, passed each incoming frame through the `yolov8n.pt` (YOLOv8 Nano) model, and displayed the annotated frames in a real-time window.

## Results & Bonus Implementations

### Objects Detected
During the test, the YOLO model successfully identified the following objects:
* Person
* Cell phone
* [Add any other objects you tested here, e.g., bottle, cup, chair]

### Extensions Added
1. **Name Extraction (Optional Extension):** The `yolo_stream.py` script was modified to extract the `class_id` from the YOLO bounding box results, map it to a human-readable string using `model.names`, and print the detected object names directly to the console in real-time.
2. **Image Logging (Bonus Task):** An automated alerting feature was added. If the script detects a "person" in the frame, it triggers an event that uses OpenCV's `cv2.imwrite()` to save a snapshot of the annotated frame locally. The files are saved sequentially (e.g., `person_detected_01.jpg`, `person_detected_02.jpg`). 

### Problems Encountered & Fixes
**Problem:** Initially encountered an `Error: Could not open stream.` when trying to run the YOLO script. 
**Fix:** Because both the sender and receiver were running on the same machine, the IP address in `yolo_stream.py` needed to be changed from the example network IP (e.g., `192.168.1.20`) to the localhost address (`127.0.0.1`). Additionally, the issue was resolved by ensuring the Flask stream (`app.py`) was kept actively running in one terminal while `yolo_stream.py` was executed in a completely separate, concurrent terminal.

<img width="941" height="206" alt="Screenshot 2026-04-15 223352" src="https://github.com/user-attachments/assets/2bca8275-c9bd-4b05-9e5c-bb3562abfc41" />

<img width="962" height="206" alt="Screenshot 2026-04-15 223521" src="https://github.com/user-attachments/assets/340300b3-9565-4bfe-9e82-d5f2e87a78c9" />

<img width="852" height="987" alt="Screenshot 2026-04-15 223619" src="https://github.com/user-attachments/assets/eca025fe-4e89-49bc-8ad0-8047ab3adb35" />

<img width="970" height="211" alt="Screenshot 2026-04-15 224712" src="https://github.com/user-attachments/assets/39f6d6e5-6393-4a71-8795-d30686995ffb" />


<img width="680" height="221" alt="Screenshot 2026-04-15 223638" src="https://github.com/user-attachments/assets/ad2558eb-ea23-42f7-a085-cf1265815ad9" />





