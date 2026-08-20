# Computer Vision Month 2 - Task 4

## Facial Emotion Recognition using FER-2013

Student: Mehak Zahra  
Internship: Arch Technologies  
Environment: Visual Studio Code on Windows

This project trains a Convolutional Neural Network (CNN) to classify facial expressions into the seven FER-2013 emotion categories. It includes training, evaluation, a confusion matrix, a classification report, model saving, and single-image prediction.

## Dataset

Download FER-2013 from Kaggle:

https://www.kaggle.com/datasets/msambare/fer2013

After downloading, extract it so the project looks like this:

```text
Task_4_Facial_Emotion_Recognition/
|-- dataset/
|   |-- train/
|   |   |-- angry/
|   |   |-- disgust/
|   |   |-- fear/
|   |   |-- happy/
|   |   |-- neutral/
|   |   |-- sad/
|   |   `-- surprise/
|   `-- test/
|       |-- angry/
|       |-- disgust/
|       |-- fear/
|       |-- happy/
|       |-- neutral/
|       |-- sad/
|       `-- surprise/
|-- facial_emotion_recognition.py
|-- predict_emotion.py
`-- requirements.txt
```

The dataset contains 48x48 grayscale face images. Kaggle lists 28,709 training images and 3,589 public test images, with seven emotion classes.

## VS Code Setup - Windows CMD

Open the project folder in VS Code. In the VS Code terminal run:

```cmd
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

PyTorch currently supports Python 3.10-3.14 on Windows, so Python 3.13 is supported by the current Windows builds.

## Train and Evaluate

```cmd
python facial_emotion_recognition.py --epochs 10
```

For a quick test before a full run:

```cmd
python facial_emotion_recognition.py --epochs 1
```

CPU training can take time. If a supported NVIDIA CUDA setup is available, the script automatically uses CUDA; otherwise it uses the CPU.

## Output

After training, the `output` folder contains:

- `best_fer2013_cnn.pth` - best trained CNN checkpoint
- `training_history.png` - accuracy and loss graphs
- `confusion_matrix.png` - class-by-class evaluation
- `classification_report.txt` - precision, recall and F1-score
- `metrics.json` - best test accuracy

These output images and terminal results are suitable screenshots for the internship report.

## Predict One Image

After training, select a face image and run:

```cmd
python predict_emotion.py "path\to\face_image.jpg"
```

Example output:

```text
Predicted emotion: happy
Confidence: 87.42%
```

Actual confidence depends on the trained model and image.

## Notes

- Dataset images and the trained `.pth` model should normally not be pushed to GitHub because they can be large.
- Accuracy varies with training time, hardware, random initialization, and hyperparameters.
- This is an educational facial-expression classifier and should not be treated as a reliable detector of a person's internal emotional state.
