from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolov8n.pt")  # YOLOv8 Nano model

# Perform object detection on your own image
results = model("/home/jetson/o.png")  # Replace with the path to your image

# Display and save results
for result in results:
    result.show()  # Display the image with bounding boxes
    result.save("output.jpg")  # Save the results to a file
