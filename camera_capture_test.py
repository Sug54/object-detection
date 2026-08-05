import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not found")
    exit()

print("Camera connected")

ret, frame = camera.read()

if ret:
    print("Frame captured!")
    print("Resolution:", frame.shape)

    cv2.imwrite("test_image.jpg", frame)
    print("Saved test_image.jpg")

else:
    print("Failed to capture frame")

camera.release()
