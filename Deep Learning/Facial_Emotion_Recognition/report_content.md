# Report Content - Facial Emotion Recognition using FER-2013

## Student Information

- Name: Mehak Zahra
- Internship: Arch Technologies
- Domain: Deep Learning
- Month: 2
- Task: 4 - Facial Emotion Recognition
- Phone: 03322136800

Add your email address on the final report front page before submission.

## 1. Objective

The objective of this project is to develop and evaluate a Convolutional Neural Network that recognizes facial expressions from FER-2013 images. The network classifies each image into one of seven categories: angry, disgust, fear, happy, neutral, sad and surprise.

## 2. Dataset

FER-2013 contains 48 by 48-pixel grayscale facial images. The dataset is organized into training and testing directories, with one folder for every expression class. The images are loaded through PyTorch ImageFolder.

## 3. Data Preprocessing

Each image is converted to grayscale, resized to 48 by 48 pixels, converted into a tensor and normalized. Random horizontal flipping and small rotations are applied to training images as data augmentation. Test images are processed without random augmentation.

## 4. CNN Architecture

The model contains three convolutional blocks. Each block combines convolution, batch normalization, ReLU activation and max pooling. The extracted features are flattened and passed through a fully connected layer. Dropout is used to reduce overfitting, and the final layer produces scores for seven emotion classes.

## 5. Training

Cross-entropy loss is used for multi-class classification and Adam is used for optimization. Training and test accuracy are recorded after every epoch. The checkpoint that obtains the highest test accuracy is saved for later inference.

## 6. Evaluation

The system generates a classification report containing precision, recall and F1-score. It also produces a confusion matrix and training-history charts. These outputs make it possible to compare performance across emotion categories and observe learning over time.

## 7. Results

Insert the best test accuracy printed by your completed training run. Add the following screenshots:

1. VS Code terminal showing the training epochs.
2. Final best test accuracy and classification report.
3. `output/training_history.png`.
4. `output/confusion_matrix.png`.
5. Optional prediction on a new facial image.

Do not add a made-up accuracy before running the model.

## 8. Conclusion

This project demonstrates the complete deep-learning workflow for image classification: dataset preparation, image preprocessing, data augmentation, CNN construction, model training, evaluation, visualization, checkpoint saving and inference. It provides practical experience with PyTorch and facial-expression recognition.

## 9. Tools and Technologies

- Python
- Visual Studio Code
- PyTorch and Torchvision
- NumPy
- Matplotlib
- scikit-learn
- Pillow

## 10. References

- https://pytorch.org/get-started/locally/
- https://www.kaggle.com/datasets/msambare/fer2013
