"""Basic OCR System - Arch Technologies Computer Vision, Month 2, Task 3."""

import argparse
from pathlib import Path
import shutil

import cv2
import numpy as np
import pytesseract
from pytesseract import Output


OUTPUT_DIR = Path("output")


def configure_tesseract() -> str:
    """Locate Tesseract on Windows/Linux and configure pytesseract."""
    detected = shutil.which("tesseract")
    candidates = [
        detected,
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    ]

    for candidate in candidates:
        if candidate and Path(candidate).exists():
            pytesseract.pytesseract.tesseract_cmd = candidate
            return candidate

    raise FileNotFoundError(
        "Tesseract OCR was not found. Install Tesseract first, then rerun this program. "
        "See README.md for the Windows setup steps."
    )


def create_demo_image(path: Path) -> None:
    """Create a printed-text image so the project can be demonstrated immediately."""
    canvas = np.full((360, 1200, 3), 255, dtype=np.uint8)
    lines = [
        "ARCH TECHNOLOGIES",
        "Computer Vision OCR",
        "Month 2 - Task 3",
    ]
    y_positions = [100, 210, 320]

    for text, y in zip(lines, y_positions):
        cv2.putText(
            canvas,
            text,
            (55, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.8,
            (20, 20, 20),
            4,
            cv2.LINE_AA,
        )

    cv2.imwrite(str(path), canvas)


def preprocess_image(image: np.ndarray) -> np.ndarray:
    """Improve OCR readability using grayscale, resizing, denoising and thresholding."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    enlarged = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    blurred = cv2.GaussianBlur(enlarged, (3, 3), 0)
    processed = cv2.threshold(
        blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]
    return processed


def run_ocr(image_path: Path) -> None:
    """Extract text, draw confident word boxes, and save OCR results."""
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    OUTPUT_DIR.mkdir(exist_ok=True)
    processed = preprocess_image(image)

    config = "--oem 3 --psm 6"
    extracted_text = pytesseract.image_to_string(processed, lang="eng", config=config)
    data = pytesseract.image_to_data(
        processed, lang="eng", config=config, output_type=Output.DICT
    )

    annotated = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)
    confidences = []

    for index, word in enumerate(data["text"]):
        word = word.strip()
        try:
            confidence = float(data["conf"][index])
        except (TypeError, ValueError):
            confidence = -1

        if word and confidence >= 30:
            x = data["left"][index]
            y = data["top"][index]
            width = data["width"][index]
            height = data["height"][index]
            cv2.rectangle(annotated, (x, y), (x + width, y + height), (0, 180, 0), 2)
            cv2.putText(
                annotated,
                word,
                (x, max(20, y - 8)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 120, 0),
                1,
                cv2.LINE_AA,
            )
            confidences.append(confidence)

    processed_path = OUTPUT_DIR / "preprocessed_image.png"
    annotated_path = OUTPUT_DIR / "ocr_result.png"
    text_path = OUTPUT_DIR / "extracted_text.txt"

    cv2.imwrite(str(processed_path), processed)
    cv2.imwrite(str(annotated_path), annotated)
    text_path.write_text(extracted_text.strip() + "\n", encoding="utf-8")

    average_confidence = float(np.mean(confidences)) if confidences else 0.0

    print("\n========== EXTRACTED TEXT ==========")
    print(extracted_text.strip() or "[No text recognized]")
    print("====================================")
    print(f"Detected words: {len(confidences)}")
    print(f"Average word confidence: {average_confidence:.2f}%")
    print(f"Saved: {processed_path}")
    print(f"Saved: {annotated_path}")
    print(f"Saved: {text_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract text from an image using OCR.")
    parser.add_argument(
        "--image",
        type=Path,
        help="Path to a printed or handwritten image. Omit to use the generated demo image.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tesseract_path = configure_tesseract()
    print(f"Tesseract detected: {tesseract_path}")

    image_path = args.image
    if image_path is None:
        image_path = Path("sample_printed_text.png")
        if not image_path.exists():
            create_demo_image(image_path)
            print(f"Created demo image: {image_path}")

    print(f"Processing image: {image_path}")
    run_ocr(image_path)


if __name__ == "__main__":
    main()
