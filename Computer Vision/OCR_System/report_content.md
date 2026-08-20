# Computer Vision — Month 2, Task 3

## Optical Character Recognition (OCR)

### Objective

The objective is to build a Python OCR system that extracts text from images containing printed or handwritten text using OpenCV for preprocessing and Tesseract for recognition.

### Dataset and test images

The application supports general JPG/PNG images and includes a generated printed-text image for immediate testing. For handwritten evaluation, sample images can be selected from the IAM Handwritten Forms Dataset on Kaggle, as specified in the internship brief.

### Tools and technologies

- Python
- Visual Studio Code
- OpenCV
- Tesseract OCR
- pytesseract
- NumPy

### Methodology

The input image is loaded with OpenCV and converted to grayscale. It is enlarged to improve character resolution, smoothed with a Gaussian filter, and converted to a binary image using Otsu thresholding. The processed image is passed to Tesseract with the English language model and page-segmentation mode 6.

Tesseract returns both extracted text and word-level recognition data. Words above a confidence threshold are surrounded by bounding boxes and labeled on an annotated result image. The application saves the preprocessed image, annotated OCR image, and extracted text while also reporting average word confidence in the terminal.

### Result

The OCR system implements a complete computer-vision text-extraction workflow and produces visual and text outputs that can be inspected directly. Printed demo text provides a reliable functional test, while IAM samples allow the effect of handwriting style on OCR accuracy to be demonstrated.

### Screenshot checklist

- Source code in VS Code
- OCR terminal output and confidence
- Original input image
- Preprocessed binary image
- Annotated OCR result
- Optional IAM handwritten result
