# Object Detection (YOLO + Flask)

Live object detection from a webcam using [Ultralytics YOLO11](https://docs.ultralytics.com/) and a Flask web interface. Frames are captured from the camera, run through the model with object tracking, and streamed to the browser with bounding boxes drawn on each detection.

## Requirements

- Python 3.13+ (tested with the included virtual environment)
- A connected USB webcam (default device index `0`)
- Linux with camera access (e.g. Raspberry Pi)

## Setup

### 1. Activate the virtual environment

**Always activate the virtual environment before running any scripts in this folder.**

From the `object_detection` directory:

```bash
cd object_detection
source .venv/bin/activate
```

Your shell prompt should show `(.venv)` when the environment is active.

To deactivate when you are done:

```bash
deactivate
```

### 2. Create the virtual environment (first time only)

If `.venv` does not exist yet, create and install dependencies:

```bash
cd object_detection
python3 -m venv .venv
source .venv/bin/activate
pip install flask ultralytics opencv-python
```

The YOLO weights file `yolo11n.pt` is included in this folder. On first run, Ultralytics may download additional model assets if needed.

## Running the app

With the virtual environment activated:

```bash
python app.py
```

Then open a browser to:

- **Local:** [http://localhost:5000](http://localhost:5000)
- **From another device on the network:** `http://<your-pi-ip>:5000`

The page shows a live MJPEG stream with detected objects labeled and tracked across frames. Detection details (class name, confidence, object count) are printed to the terminal.

Press `Ctrl+C` in the terminal to stop the server.

## Camera test scripts

Use these to verify the webcam works before running the full detection pipeline. Activate the virtual environment first.

**Quick camera check** — opens a live preview window (press `q` to quit):

```bash
python camera_test.py
```

**Single-frame capture** — saves one frame as `test_image.jpg`:

```bash
python camera_capture_test.py
```

## Project structure

```
object_detection/
├── app.py                  # Flask web server
├── yolo_camera.py          # YOLO model, camera capture, and frame generator
├── templates/
│   └── index.html          # Web page with live video feed
├── yolo11n.pt              # YOLO11 nano model weights (in use)
├── yolo11s.pt              # YOLO11 small model weights (alternate)
├── camera_test.py          # Live camera preview utility
├── camera_capture_test.py  # Single-frame capture utility
└── .venv/                  # Python virtual environment (do not commit)
```

## Configuration

Detection settings live in `yolo_camera.py`:

| Setting   | Default      | Description                          |
|-----------|--------------|--------------------------------------|
| Model     | `yolo11n.pt` | YOLO weights file                    |
| Camera    | `0`          | OpenCV device index                  |
| Resolution| 640×480      | Capture size                         |
| Confidence| `0.7`        | Minimum detection confidence         |
| IoU       | `0.5`        | Overlap threshold for NMS            |
| Tracking  | enabled      | Objects persist with IDs across frames |

To use the larger model, change the model path in `yolo_camera.py`:

```python
model = YOLO("yolo11s.pt")
```

## Troubleshooting

**"Camera not found"**
- Confirm the webcam is plugged in: `ls /dev/video*`
- Make sure no other process is using the camera
- Try a different device index in `yolo_camera.py` (e.g. `cv2.VideoCapture(1)`)

**Slow inference on Raspberry Pi**
- The included setup uses CPU-only PyTorch (`torch 2.13.0+cpu`), which is expected on ARM devices
- Use `yolo11n.pt` (nano) rather than `yolo11s.pt` for better frame rates
- Lower resolution or raise the confidence threshold to reduce work per frame

**Module not found errors**
- Confirm the virtual environment is activated (`source .venv/bin/activate`)
- Reinstall dependencies: `pip install flask ultralytics opencv-python`

**Cannot reach the web page from another device**
- The server binds to `0.0.0.0:5000` by default
- Check firewall rules and use the Pi's IP address, not `localhost`
