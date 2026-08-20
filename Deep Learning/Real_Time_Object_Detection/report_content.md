# Report Content - Real-Time Object Detection using YOLO

## Student Information

- Name: Mehak Zahra
- Internship: Arch Technologies
- Domain: Deep Learning
- Month: 2
- Task: 3 - Real-Time Object Detection using YOLO
- Phone: 03322136800

Add your email address on the final report front page before submission.

## 1. Objective

The objective of this task is to implement a real-time deep-learning object detector using YOLO. The system captures frames from a webcam, identifies common objects, draws bounding boxes, class names and confidence scores, and displays the annotated frames in real time.

## 2. Model

The implementation uses the pretrained Ultralytics YOLO11n object-detection model. YOLO is designed to perform object localization and classification efficiently in a single detection pipeline. The nano variant was selected because its smaller size makes it practical for real-time student demonstrations and CPU-based systems.

## 3. Implementation

The Python application loads the pretrained YOLO model through the Ultralytics package. OpenCV captures frames from the computer webcam. Each frame is passed to the detector and the returned boxes, labels and confidence values are rendered on the frame. The program also calculates approximate frames per second and displays the number of objects detected. The user can press S to save an annotated screenshot and Q to quit.

An additional image-detection script is included so that the same model can be tested on a still photograph when a webcam is unavailable.

## 4. Output and Evaluation

The real-time output consists of a camera window containing object bounding boxes, predicted COCO class labels and confidence scores. Practical evaluation can be demonstrated by placing several common objects in view and checking whether the detector identifies them correctly.

## 5. Screenshots to Add to Final Report

1. VS Code terminal after the YOLO model loads.
2. Real-time webcam detection window.
3. Saved `output/detection_1.jpg` showing bounding boxes.
4. Optional image-detection terminal results.

## 6. Conclusion

This task demonstrates how a pretrained deep-learning object detector can be integrated into a real-time computer-vision application. It provides practical experience with YOLO inference, OpenCV video capture, bounding-box visualization, confidence scores and model deployment in a local VS Code environment.

## 7. Tools and Technologies

- Python
- Visual Studio Code
- Ultralytics YOLO11
- PyTorch (installed as an Ultralytics dependency)
- OpenCV

## 8. References

- https://docs.ultralytics.com/modes/predict/
- https://docs.ultralytics.com/models/yolo11/
