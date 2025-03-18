from ultralytics import YOLO
import cv2

# Load a pretrained YOLO model
model = YOLO("yolov8n.pt")  # YOLOv8 Nano model

# GStreamer pipeline for CSI camera
gstreamer_pipeline = (
    "nvarguscamerasrc ! "
    "video/x-raw(memory:NVMM), width=1280, height=720, framerate=30/1 ! "
    "nvvidconv ! video/x-raw, format=BGRx ! "
    "videoconvert ! video/x-raw, format=BGR ! appsink"
)

# Open the CSI camera using the GStreamer pipeline
cap = cv2.VideoCapture(gstreamer_pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Main loop for real-time object detection
while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Perform object detection on the frame
    results = model(frame)

    # Display the results
    annotated_frame = results[0].plot()  # Get the annotated frame
    cv2.imshow('YOLOv8 Real-Time Object Detection', annotated_frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
