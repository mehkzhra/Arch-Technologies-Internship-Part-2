# Deep Learning Month 2 - Task 3

## Real-Time Object Detection using YOLO

Student: Mehak Zahra  
Internship: Arch Technologies  
Domain: Deep Learning  
Environment: Visual Studio Code on Windows

This project uses a pretrained Ultralytics YOLO11n model for real-time object detection. The webcam application draws bounding boxes, class labels and confidence scores, displays the number of detected objects and approximate FPS, and can save screenshots for the internship report.

## Why YOLO11n?

Ultralytics currently recommends YOLO11 as a mature model family and supports prediction from images, video and webcam sources. The nano model (`yolo11n.pt`) is small and suitable for a student project that may run on CPU.

## VS Code Setup on Windows

Because Windows can produce `WinError 206` when a virtual environment is inside a very long OneDrive project path, create this task's environment at a short path:

```cmd
python -m venv C:\yolo_venv
C:\yolo_venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Check the installation:

```cmd
python -c "import ultralytics, cv2; print('YOLO setup OK')"
```

## Run Real-Time Webcam Detection

```cmd
python detect_webcam.py
```

The first run automatically downloads the official `yolo11n.pt` pretrained weights if they are not already available.

Controls:

- Press `S` in the camera window to save a detection screenshot.
- Press `Q` to stop.

If camera 0 does not work:

```cmd
python detect_webcam.py --camera 1
```

## Test With an Image

Put any test photograph in the project folder and run:

```cmd
python detect_image.py "test_image.jpg"
```

The annotated result is saved as:

```text
output/image_detection_result.jpg
```

## Expected Output

The program detects common COCO objects such as person, car, chair, bottle, cup, laptop and many others. Each detected object is shown with a bounding box, class name and confidence score.

For your report, capture:

1. VS Code terminal showing successful startup.
2. Webcam window with multiple bounding boxes.
3. A saved image from `output/detection_1.jpg`.
4. Optional `detect_image.py` terminal output.

## Project Files

```text
Task_3_Real_Time_Object_Detection/
|-- detect_webcam.py
|-- detect_image.py
|-- requirements.txt
|-- README.md
|-- report_content.md
`-- output/                 # created automatically
```

## References

- Ultralytics Predict documentation: https://docs.ultralytics.com/modes/predict/
- Ultralytics YOLO11 documentation: https://docs.ultralytics.com/models/yolo11/
