import cv2

# RTSP URL
rtsp_url = 'your_rtsp_url_here'

# Open the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Define the codec and create VideoWriter object
# FourCC is a 4-byte code used to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can use other codecs like 'MJPG', 'X264', etc.
output_file = 'recorded_video.mkv'
output = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))  # Adjust resolution and framerate as needed

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Write the frame to the output video file
    output.write(frame)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
output.release()
cv2.destroyAllWindows()
