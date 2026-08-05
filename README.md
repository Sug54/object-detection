# Object Detection (YOLO)

Live object detection on a **Raspberry Pi** with a **Logitech Brio 100**, using Ultralytics YOLO and OpenCV. Run `yolo_camera.py` and a window opens immediately.

Dependencies and change history: [CHANGES.md](CHANGES.md).

## Setup

```bash
cd object-detection
python3 -m venv .venv
source .venv/bin/activate
pip install ultralytics opencv-python
```

Always activate the venv before running scripts: `source .venv/bin/activate`

## Run

```bash
python yolo_camera.py
```

Press `q` in the video window to quit.

**Camera checks**

```bash
python camera_test.py           # live preview
python camera_capture_test.py   # saves test_image.jpg
```

## Project structure

```
object-detection/
├── yolo_camera.py          # Main app
├── camera_test.py
├── camera_capture_test.py
├── README.md
├── CHANGES.md
├── yolo26n.pt              # Active model
├── yolo11n.pt / yolo11s.pt # Alternates
└── .venv/
```

## Configuration (`yolo_camera.py`)

| Setting    | Value          | Notes                          |
|------------|----------------|--------------------------------|
| Model      | `yolo26n.pt`   | Nano weights for Pi CPU        |
| Backend    | V4L2           | USB webcam on Linux/Pi         |
| Capture    | 1280×720 MJPEG | Brio 100–friendly              |
| Inference  | `imgsz=256`    | Speed vs. detection balance    |
| Confidence | `0.2`         | Lower = more boxes             |
| Mode       | `predict`      | No tracking IDs                |

## Troubleshooting

- **Camera not found:** `ls /dev/video*` — try device index `1` if needed
- **Laggy feed:** keep MJPEG; try `640×480` or lower `imgsz`
- **Few detections:** lower `conf` (e.g. `0.25`) or raise `imgsz` to `416`
- **Import errors:** activate `.venv`, then `pip install ultralytics opencv-python`
