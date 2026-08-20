# Deep Learning Month 2 - Task 4

## Facial Emotion Recognition using FER-2013

Student: Mehak Zahra  
Internship: Arch Technologies  
Domain: Deep Learning  
Environment: Visual Studio Code on Windows

This project trains a Convolutional Neural Network (CNN) on FER-2013 and classifies a face into seven expression categories: angry, disgust, fear, happy, neutral, sad and surprise. It generates accuracy/loss graphs, a confusion matrix, a classification report and a saved PyTorch model.

## Dataset Setup

Download FER-2013:

https://www.kaggle.com/datasets/msambare/fer2013

Extract it into this project with the following structure:

```text
dataset/
|-- train/
|   |-- angry/
|   |-- disgust/
|   |-- fear/
|   |-- happy/
|   |-- neutral/
|   |-- sad/
|   `-- surprise/
`-- test/
    |-- angry/
    |-- disgust/
    |-- fear/
    |-- happy/
    |-- neutral/
    |-- sad/
    `-- surprise/
```

If you already downloaded FER-2013 for Computer Vision Task 4, copy its `train` and `test` folders into this task's `dataset` folder. Do not download the dataset again.

## VS Code Setup

You can reuse the short virtual environment created for the Computer Vision FER task:

```cmd
C:\fer_venv\Scripts\activate
```

Check packages:

```cmd
python -c "import torch, torchvision, matplotlib; print('FER setup OK')"
```

If `C:\fer_venv` does not exist, create it:

```cmd
python -m venv C:\fer_venv
C:\fer_venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The short environment path avoids the Windows `WinError 206` that can occur when PyTorch is installed inside a long OneDrive path.

## Run Training

First perform a one-epoch test:

```cmd
python facial_emotion_recognition.py --epochs 1
```

After the test completes, run full training:

```cmd
python facial_emotion_recognition.py --epochs 10
```

The script uses CUDA automatically when available; otherwise it trains on CPU.

## Generated Output

The `output` folder will contain:

- `best_fer2013_cnn.pth`
- `training_history.png`
- `confusion_matrix.png`
- `classification_report.txt`
- `metrics.json`

Use the terminal result, training graph and confusion matrix as report screenshots.

## Predict a New Image

After training:

```cmd
python predict_emotion.py "path\to\face_image.jpg"
```

Example format:

```text
Predicted emotion: happy
Confidence: 87.42%
```

The actual result depends on the trained model and input image.

## Important Note

This is an educational facial-expression image classifier. A visible facial expression does not necessarily reveal a person's true internal emotional state.

## References

- PyTorch: https://pytorch.org/get-started/locally/
- FER-2013: https://www.kaggle.com/datasets/msambare/fer2013
