# Object Detection (YOLO)

Live object detection from a webcam using [Ultralytics YOLO](https://docs.ultralytics.com/). Frames are captured from the camera, run through the model with object tracking, and shown in an OpenCV window with bounding boxes drawn on each detection.

## Requirements

- Python 3.13+ (tested with the included virtual environment)
- A connected USB webcam (default device index `0`)
- Linux with camera access (e.g. Raspberry Pi) or Windows with a working webcam

## Setup

### 1. Activate the virtual environment

**Always activate the virtual environment before running any scripts in this folder.**

From the `object-detection` directory:

```bash
cd object-detection
source .venv/bin/activate
```

On Windows (PowerShell):

```powershell
cd object-detection
.\.venv\Scripts\Activate.ps1
```

Your shell prompt should show `(.venv)` when the environment is active.

To deactivate when you are done:

```bash
deactivate
```

### 2. Create the virtual environment (first time only)

If `.venv` does not exist yet, create and install dependencies:

```bash
cd object-detection
python3 -m venv .venv
source .venv/bin/activate
pip install ultralytics opencv-python
```

The YOLO weights file is included in this folder. On first run, Ultralytics may download additional model assets if needed.

## Running the app

With the virtual environment activated:

```bash
python yolo_camera.py
```

A window opens immediately with the live camera feed and YOLO detections. Detection details (class name, confidence, object count) are also printed to the terminal.

Press `q` in the video window to quit.

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
object-detection/
├── yolo_camera.py          # YOLO model, camera capture, and live window
├── yolo26n.pt              # YOLO nano model weights (in use)
├── camera_test.py          # Live camera preview utility
├── camera_capture_test.py  # Single-frame capture utility
└── .venv/                  # Python virtual environment (do not commit)
```

## Configuration

Detection settings live in `yolo_camera.py`:

| Setting    | Default      | Description                           |
|------------|--------------|---------------------------------------|
| Model      | `yolo26n.pt` | YOLO weights file                     |
| Camera     | `0`          | OpenCV device index                   |
| Resolution | 256×256      | Capture size                          |
| Confidence | `0.6`        | Minimum detection confidence          |
| Tracking   | enabled      | Objects persist with IDs across frames|

To use a different model, change the model path in `yolo_camera.py`:

```python
model = YOLO("yolo11s.pt")
```

## Troubleshooting

**"Camera not found"**
- Confirm the webcam is plugged in
- Make sure no other process is using the camera
- Try a different device index in `yolo_camera.py` (e.g. `cv2.VideoCapture(1)`)

**Slow inference on Raspberry Pi**
- The included setup uses CPU-only PyTorch, which is expected on ARM devices
- Use the nano model rather than a larger one for better frame rates
- Lower resolution or raise the confidence threshold to reduce work per frame

**Module not found errors**
- Confirm the virtual environment is activated
- Reinstall dependencies: `pip install ultralytics opencv-python`
