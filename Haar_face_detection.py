# MIT License
# Copyright (c) 2019-2022 JetsonHacks

import cv2

# gstreamer_pipeline function returns a GStreamer pipeline for capturing video from the CSI camera.
# The function takes parameters that define the capture resolution, display resolution, frame rate, and camera flip.
# The default values are set for 1920x1080 resolution at 30 fps, with a flip method of 0.

def gstreamer_pipeline(
    capture_width=1920,  # Capture width for the camera resolution
    capture_height=1080,  # Capture height for the camera resolution
    display_width=960,  # Width of the display window
    display_height=540,  # Height of the display window
    framerate=30,  # Frame rate for capturing the video
    flip_method=0,  # Flip method for the camera image (0: no flip, 2: flip vertically)
):
    # Return a formatted string representing the GStreamer pipeline.
    # The pipeline specifies the video source, processing, and the format for output.
    return (
        "nvarguscamerasrc ! "  # Camera source for the NVIDIA Jetson platform
        "video/x-raw(memory:NVMM), "  # Video format and memory (NVMM for GPU memory)
        "width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "  # Resolution and frame rate
        "nvvidconv flip-method=%d ! "  # Flip method for the image (vertical flip, etc.)
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "  # Output format (BGRx color space)
        "videoconvert ! "  # Convert to BGR format for OpenCV
        "video/x-raw, format=(string)BGR ! appsink drop=True"  # Drop frames if processing can't keep up, pass to OpenCV
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


# face_detect function captures video from the camera and performs face and eye detection.
def face_detect():
    window_title = "Face Detect"  # Title of the OpenCV window where the video is displayed

    # Load the pre-trained face and eye classifiers from OpenCV
    face_cascade = cv2.CascadeClassifier(
        "/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml"
    )
    eye_cascade = cv2.CascadeClassifier(
        "/usr/share/opencv4/haarcascades/haarcascade_eye.xml"
    )

    # Open the video stream using the GStreamer pipeline defined earlier
    video_capture = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)
    
    # Check if the video capture object is successfully opened
    if video_capture.isOpened():
        try:
            # Create a window for displaying the video stream
            cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)

            # Infinite loop to continuously read frames from the camera
            while True:
                ret, frame = video_capture.read()  # Read a frame from the camera
                if not ret:
                    break  # If frame isn't captured, exit the loop

                # Convert the captured frame to grayscale for face detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Perform face detection using the face cascade
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                # For each detected face, draw a rectangle and detect eyes within the face region
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw rectangle around the face
                    roi_gray = gray[y : y + h, x : x + w]  # Region of interest (ROI) in grayscale
                    roi_color = frame[y : y + h, x : x + w]  # ROI in color (original frame)
                    
                    # Detect eyes within the face region
                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    
                    # Draw rectangles around detected eyes
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(
                            roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2
                        )
                
                # Check if the window is still open, using WND_PROP_AUTOSIZE under GTK+ for Jetson
                if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                    cv2.imshow(window_title, frame)  # Show the frame in the OpenCV window
                else:
                    break  # If window is closed, break the loop

                # Wait for a key press; if ESC or 'q' is pressed, break the loop
                keyCode = cv2.waitKey(10) & 0xFF
                if keyCode == 27 or keyCode == ord('q'):  # ESC or 'q' to quit
                    break
        finally:
            # Release the video capture object and close any OpenCV windows
            video_capture.release()
            cv2.destroyAllWindows()
    else:
        print("Unable to open camera")  # If the camera couldn't be opened, print an error message


if __name__ == "__main__":
    face_detect()  # Run the face detection function when the script is executed
