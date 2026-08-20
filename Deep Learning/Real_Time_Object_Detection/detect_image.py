"""Run YOLO object detection on one image and save the annotated result."""

from __future__ import annotations

import argparse
from pathlib import Path

import cv2
from ultralytics import YOLO


PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "output"


def main() -> None:
    parser = argparse.ArgumentParser(description="YOLO image object detection")
    parser.add_argument("image", type=Path, help="Path to the input image")
    parser.add_argument("--model", default="yolo11n.pt")
    parser.add_argument("--conf", type=float, default=0.40)
    args = parser.parse_args()

    if not args.image.is_file():
        raise FileNotFoundError(f"Input image not found: {args.image}")

    OUTPUT_DIR.mkdir(exist_ok=True)
    model = YOLO(args.model)
    result = model.predict(str(args.image), conf=args.conf, verbose=False)[0]
    annotated = result.plot()
    output_path = OUTPUT_DIR / "image_detection_result.jpg"
    cv2.imwrite(str(output_path), annotated)

    print(f"Objects detected: {len(result.boxes)}")
    for box in result.boxes:
        class_id = int(box.cls[0].item())
        confidence = float(box.conf[0].item())
        print(f"- {model.names[class_id]}: {confidence:.2%}")
    print(f"Saved result: {output_path}")


if __name__ == "__main__":
    main()
