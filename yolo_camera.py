from ultralytics import YOLO
import cv2
import sys

# Load YOLO model once
model = YOLO("yolo26n.pt")

# V4L2 on Linux/Pi, DirectShow on Windows
if sys.platform == "win32":
    backend = cv2.CAP_DSHOW
else:
    backend = cv2.CAP_V4L2

camera = cv2.VideoCapture(0, backend)

# Brio 100 is happiest at 720p/30; MJPEG keeps USB bandwidth down on a Pi
camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
camera.set(cv2.CAP_PROP_FPS, 30)
camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)

if not camera.isOpened():
    raise Exception("Camera not found")

print("Camera opened. Press 'q' to quit.")

while True:
    # Drop stale buffered frames so the window stays near live
    camera.grab()
    ret, frame = camera.retrieve()

    if not ret:
        print("Failed to grab frame")
        break

    # imgsz=320 keeps the Pi usable; conf=0.35 catches more objects
    results = model.predict(
        frame,
        imgsz=320,
        conf=0.35,
        verbose=False,
    )

    annotated_frame = results[0].plot()
    cv2.imshow("YOLO Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
