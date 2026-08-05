# Changes & Requirements

Target: Raspberry Pi + Logitech Brio 100.

## Requirements

```bash
pip install ultralytics opencv-python
```

- `ultralytics` — YOLO inference
- `opencv-python` — camera + live window
- Model in use: `yolo26n.pt`
- Flask is not used

## What changed and why

1. **Removed Flask (`app.py`, `templates/`)**  
   Camera opens right away from `yolo_camera.py` instead of through a browser.

2. **OpenCV window instead of a web stream**  
   Simpler on the Pi; press `q` to quit.

3. **Pi / Brio 100 tuning**
   - MJPEG 1280×720 @ 30 — less USB stutter than raw video
   - V4L2 backend only (Pi/Linux — no Windows path)
   - Small camera buffer + grab/retrieve — show the latest frame, not a delayed one
   - `imgsz=320`, `conf=0.35` — more detections than 256/0.6, still fast enough on Pi CPU
   - `predict` instead of `track` — less CPU
   - No per-frame prints / Ultralytics verbose — those were lagging the feed
