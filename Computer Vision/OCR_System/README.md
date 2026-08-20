# Optical Character Recognition (OCR) System

Arch Technologies Internship — Computer Vision, Month 2, Task 3.

## Project overview

This VS Code project extracts text from printed or handwritten images using OpenCV preprocessing and the Tesseract OCR engine. It converts an image to grayscale, enlarges and denoises it, applies Otsu thresholding, extracts English text, draws word-level bounding boxes, and saves the results.

If no input image is provided, the program automatically creates a printed-text demo image so the full workflow can be tested immediately.

## Technologies used

- Python
- Visual Studio Code
- OpenCV
- Tesseract OCR
- pytesseract
- NumPy

## Step 1: Install Tesseract on Windows

`pytesseract` is only a Python wrapper; the Tesseract OCR application must also be installed on Windows.

Tesseract's official documentation points Windows users to the current Windows installers maintained by UB Mannheim:

https://tesseract-ocr.github.io/tessdoc/Installation.html

Install Tesseract using the standard location when possible:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

The Python program automatically checks this common location, so manually editing the script should not be necessary.

Verify from CMD if Tesseract is on PATH:

```cmd
tesseract --version
```

If this command is not recognized but Tesseract exists under `C:\Program Files\Tesseract-OCR`, the Python script can still detect it.

## Step 2: Open the project in VS Code

Extract this project, open VS Code, and select **File → Open Folder**.

Open **Terminal → New Terminal**.

Create a virtual environment:

```cmd
python -m venv venv
```

Activate it:

```cmd
venv\Scripts\activate
```

Install Python dependencies:

```cmd
pip install -r requirements.txt
```

## Step 3: Run the built-in demo

```cmd
python ocr_system.py
```

The program creates `sample_printed_text.png`, processes it, prints the recognized text in the terminal, and saves OCR results inside the `output` folder.

## Test your own image

Place an image in the project folder or `input_images` folder and run:

```cmd
python ocr_system.py --image "input_images\my_image.png"
```

JPG, JPEG, and PNG images supported by OpenCV can be used.

## IAM handwritten dataset testing

The internship brief mentions the IAM Handwritten Forms Dataset. A Kaggle copy is available here:

https://www.kaggle.com/datasets/naderabdelghany/iam-handwritten-forms-dataset

For a lightweight internship demo, download the dataset from Kaggle, copy one or more form images into `input_images`, and run the same `--image` command. Tesseract is primarily a general OCR engine, so handwritten recognition quality can vary by writing style and image quality.

## Generated files

```text
sample_printed_text.png
output\preprocessed_image.png
output\ocr_result.png
output\extracted_text.txt
```

## Screenshot requirements

Capture screenshots showing:

- VS Code with `ocr_system.py` open
- Terminal showing extracted text and OCR confidence
- Original/sample input image
- `preprocessed_image.png`
- `ocr_result.png` with bounding boxes
- If possible, one IAM handwritten example result

Recommended screenshot names:

```text
ocr_terminal_output.png
ocr_preprocessed.png
ocr_result.png
```

## Folder structure

```text
OCR System/
├── ocr_system.py
├── requirements.txt
├── README.md
├── report_content.md
├── input_images/
│   └── README.txt
├── sample_printed_text.png       # generated after running
└── output/                        # generated after running
    ├── preprocessed_image.png
    ├── ocr_result.png
    └── extracted_text.txt
```

Do not upload the `venv` folder to GitHub.

## Concepts demonstrated

Image loading, grayscale conversion, resizing, Gaussian denoising, thresholding, OCR, page segmentation, text extraction, confidence scores, word bounding boxes, and result export.
