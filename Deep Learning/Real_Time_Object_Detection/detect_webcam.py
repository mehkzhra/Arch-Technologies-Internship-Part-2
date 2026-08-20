"""Real-time object detection from a webcam using a pretrained YOLO model."""

from __future__ import annotations

import argparse
import time
from pathlib import Path

import cv2
from ultralytics import YOLO


PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "output"


def main() -> None:
    parser = argparse.ArgumentParser(description="Real-time YOLO object detection")
    parser.add_argument("--camera", type=int, default=0, help="Webcam index, normally 0")
    parser.add_argument("--model", default="yolo11n.pt", help="Ultralytics YOLO checkpoint")
    parser.add_argument("--conf", type=float, default=0.40, help="Minimum confidence threshold")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(exist_ok=True)
    print(f"Loading {args.model} ...")
    model = YOLO(args.model)

    camera = cv2.VideoCapture(args.camera)
    if not camera.isOpened():
        raise RuntimeError(
            "Could not open the webcam. Close other camera apps and try again. "
            "If needed, try --camera 1."
        )

    print("Camera started. Press S to save a result screenshot, Q to quit.")
    previous_time = time.perf_counter()
    saved_count = 0

    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                print("Could not read a frame from the webcam.")
                break

            result = model.predict(frame, conf=args.conf, verbose=False)[0]
            annotated = result.plot()

            now = time.perf_counter()
            fps = 1.0 / max(now - previous_time, 1e-9)
            previous_time = now
            object_count = len(result.boxes)
            cv2.putText(
                annotated,
                f"Objects: {object_count} | FPS: {fps:.1f}",
                (12, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
                (0, 255, 0),
                2,
                cv2.LINE_AA,
            )

            cv2.imshow("YOLO Real-Time Object Detection", annotated)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            if key == ord("s"):
                saved_count += 1
                path = OUTPUT_DIR / f"detection_{saved_count}.jpg"
                cv2.imwrite(str(path), annotated)
                print(f"Saved screenshot: {path}")
    finally:
        camera.release()
        cv2.destroyAllWindows()

    print("Object detection stopped.")


if __name__ == "__main__":
    main()
