import cv2
from FaceDetector import FaceDetector

# Initialize the face detector with the Haar Cascade XML file
face_detector = FaceDetector('haarcascade_frontalface_default.xml')

# Initialize video capture with the default webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    _, frame = cap.read()

    # Detect faces
    faces = face_detector.detect_faces(frame)

    # Draw rectangles around faces
    frame_with_faces = face_detector.draw_faces(frame, faces)

    # Display the frame with the detected faces
    cv2.imshow('Live Feed', frame_with_faces)

    # Wait for a key press and check if the user pressed 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break