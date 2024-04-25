#Created by Garthi
import cv2

# RTSP URL
rtsp_url = 'your_rtsp_url_here' #Add the Camera Link Here 

# Open the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

#to get the frame size and frame rate
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
# FourCC is a 4-byte code used to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can use other codecs like 'MJPG', 'X264', etc.
output_file = 'recorded_video.mkv'
output = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))  # Adjust resolution and framerate as needed

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Write the frame to the output video file
    output.write(frame)

    # Display the frame
    #cv2.imshow('Frame', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
output.release()
cv2.destroyAllWindows()
