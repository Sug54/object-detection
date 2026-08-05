from ultralytics import YOLO
import cv2

# Load YOLO model once
model = YOLO("yolo26n.pt")

# Open camera once
camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)

if not camera.isOpened():
    raise Exception("Camera not found")

print("Camera opened. Press 'q' to quit.")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLO
    results = model.track(
        frame,
        imgsz=256,
        persist=True,
        conf=0.6,
    )

    # Print detections
    for box in results[0].boxes:
        cls = int(box.cls[0])
        name = model.names[cls]
        confidence = float(box.conf[0])
        print(f"{name}: {confidence:.2f}")

    print("Objects detected:", len(results[0].boxes))

    # Draw boxes and show in a window
    annotated_frame = results[0].plot()
    cv2.imshow("YOLO Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
