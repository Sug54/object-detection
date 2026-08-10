from ultralytics import YOLO
import cv2

model = YOLO("yolo26n.pt")

# V4L2 is the USB webcam path on Raspberry Pi / Linux
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)

# Brio 100 set at 720p/30; MJPG keeps USB bandwidth down
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)

if not camera.isOpened():
    print("Camera not found")
    exit()

print("Camera opened. Press 'q' to quit.")

while True:
    
    ret, frame = camera.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Smaller YOLO input improves Raspberry Pi performance
    # Lower confidence threshold allows more detections
    results = model.predict(
        frame,
        imgsz=256,
        conf=0.2,
        verbose=False,
    )

    annotated_frame = results[0].plot()
    cv2.imshow("YOLO Object Detection", annotated_frame)

    # Detect keyboard input "q" and exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
