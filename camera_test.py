import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not found")
    exit()

print("Camera detected!")

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to get frame")
        break

    cv2.imshow("Logitech Brio 100", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
