# Report Content - Facial Emotion Recognition using FER-2013

## Student Information

- Name: Mehak Zahra
- Internship: Arch Technologies
- Domain: Computer Vision
- Month: 2
- Task: 4 - Facial Emotion Recognition
- Phone: 03322136800

Add your email address on the final report front page before submission.

## 1. Project Objective

The objective of this task is to build a computer-vision system that recognizes facial expressions using the FER-2013 dataset. A Convolutional Neural Network (CNN) is trained to classify facial images into seven emotion classes: angry, disgust, fear, happy, neutral, sad, and surprise.

## 2. Dataset

FER-2013 contains 48x48 grayscale face images. The Kaggle distribution used for this project provides a training and testing directory organized by emotion. This project loads these directories with PyTorch ImageFolder.

## 3. Pre-processing

All images are converted to one-channel grayscale, resized to 48x48 pixels, converted to tensors, and normalized. Random horizontal flipping and small rotations are applied to training images as data augmentation.

## 4. CNN Implementation

The model contains three convolution blocks. Each block uses convolution, batch normalization, ReLU activation, and max pooling. Extracted features are flattened and passed through a fully connected layer with dropout before the final seven-class output layer. Cross-entropy loss and the Adam optimizer are used for training.

## 5. Training and Evaluation

The program automatically trains on CUDA when a supported GPU is available and otherwise uses the CPU. Training and test loss/accuracy are recorded for each epoch. The checkpoint with the highest test accuracy is saved. Final evaluation produces a classification report and confusion matrix.

## 6. Output Files

The project generates a trained model checkpoint, training-history plot, confusion matrix, classification report, and metrics file. The separate prediction script loads the saved checkpoint and predicts the emotion and confidence for a new face image.

## 7. Results

Insert the final accuracy printed by your own training run here. Also insert screenshots of:

1. VS Code terminal showing training epochs.
2. Final classification report / best test accuracy.
3. `output/training_history.png`.
4. `output/confusion_matrix.png`.
5. Optional single-image prediction result.

Do not invent an accuracy value before training is completed.

## 8. Conclusion

This project demonstrates an end-to-end deep-learning workflow for facial-expression classification: dataset preparation, image preprocessing, CNN design, model training, evaluation, visualization, model persistence, and inference on a new image. It provides practical experience with PyTorch and computer-vision classification.

## 9. Tools and Technologies

- Python
- Visual Studio Code
- PyTorch / Torchvision
- NumPy
- Matplotlib
- scikit-learn
- Pillow

## 10. References

- PyTorch: https://pytorch.org/get-started/locally/
- FER-2013 Kaggle dataset: https://www.kaggle.com/datasets/msambare/fer2013
