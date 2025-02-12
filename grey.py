# Import the OpenCV library for computer vision tasks
import cv2

# Function to generate a GStreamer pipeline string to capture camera frames
def gstreamer_pipeline(
    sensor_id=0,                  # Camera sensor ID (default is 0, which is usually the first connected camera)
    capture_width=1920,           # Capture resolution width (default is 1920 pixels)
    capture_height=1080,          # Capture resolution height (default is 1080 pixels)
    display_width=960,             # Display resolution width (default is 960 pixels for displaying on screen)
    display_height=540,            # Display resolution height (default is 540 pixels for displaying on screen)
    framerate=30,                  # Frame rate in frames per second (default is 30 FPS)
    flip_method=0,                 # Flip method for the image (default is 0, meaning no flip; other values may rotate/flip the image)
):
    # Construct the GStreamer pipeline command string using the given parameters
    return (
        "nvarguscamerasrc sensor-id=%d ! "                              # 'nvarguscamerasrc' is used to access the camera sensor
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "  # Defines the video format, including resolution and framerate
        "nvvidconv flip-method=%d ! "                                      # 'nvvidconv' is used to perform transformations on the video stream (flip/rotate)
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "  # Converts the format to BGRx for OpenCV processing
        "videoconvert ! "                                                  # Converts the video to standard BGR format
        "video/x-raw, format=(string)BGR ! appsink"                          # Final step to send frames to OpenCV (appsink)
        % (
            sensor_id,              # Insert the camera sensor ID (e.g., 0 for the first camera)
            capture_width,           # Insert the width of the capture resolution
            capture_height,          # Insert the height of the capture resolution
            framerate,               # Insert the desired framerate
            flip_method,             # Insert the flip method (0 is no flip, other values apply transformations)
            display_width,           # Insert the display width for resizing the image when showing it
            display_height,          # Insert the display height for resizing the image when showing it
        )
    )

# Open the camera using the GStreamer pipeline created in the previous step
cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)

# Check if the video capture was successfully opened
if cap.isOpened():
    # If the camera is open, enter a loop to continuously capture frames
    while True:
        # 'ret' is a boolean that indicates whether the frame was successfully captured
        # 'frame' contains the actual image data (the video frame from the camera)
        ret, frame = cap.read()
        
        # If the frame was not successfully captured, 'ret' will be False
        if not ret:
            # If frame capture fails, print an error message and exit the loop
            print("Failed to capture image")
            break
        
        # 'frame' is the captured image in BGR color space
        # Convert the captured frame from BGR to grayscale (this helps reduce computational complexity)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(frame, 50, 150)

        # Display the original color frame in a window titled "Original"
        cv2.imshow("Original", frame)

        # Display the grayscale frame in a window titled "Grayscale"
        cv2.imshow("Grayscale", gray)

        cv2.imshow("Canny Edge", edges)

        # Wait for 1 millisecond for a key press event and check if it's 'q'
        # If the user presses 'q', break out of the loop and end the video capture
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object to free up the camera for other applications
    cap.release()

    # Close all OpenCV windows that were opened during the program
    cv2.destroyAllWindows()
else:
    # If the camera failed to open, print an error message
    print("Error: Unable to open camera")
