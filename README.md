# Hand Gesture Volume Control 🎵✋

## 📌 About the Project

This project is a Python application that uses **Computer Vision** and **Hand Gesture Recognition** to detect finger counts through a webcam.

The application uses **MediaPipe** to detect hand landmarks and **OpenCV** to process webcam frames and display the detected number on the screen.

The main goal of this project is to recognize specific hand gesture sequences and use them to control the system volume.

## ✨ Features

- ✋ Hand detection using MediaPipe.
- 📷 Real-time webcam processing with OpenCV.
- 🔢 Finger counting and number recognition.
- 🔄 Recognition of specific hand gesture sequences.
- 🎨 Displaying detected numbers on the webcam screen.
- 🎵 Designed to increase or decrease the system volume based on recognized gestures.

## 🖐️ How It Works

The application detects the number of raised fingers and displays the result on the webcam screen.

Two gesture sequences are used:

- **1 → 2 → 3:** Increase the system volume by 5 units.
- **3 → 2 → 1:** Decrease the system volume by 5 units.

Each complete sequence is intended to trigger one volume change.

## 🛠️ Technologies Used

- **Python** — Programming language.
- **OpenCV** — Webcam access and image processing.
- **MediaPipe** — Hand landmark detection and gesture recognition.

## 📦 Installation

First, install the required libraries:

```bash
pip install opencv-python mediapipe
```

## ▶️ How to Run

1. Clone or download this repository.
2. Install the required libraries.
3. Connect a webcam to your computer.
4. Run the Python script:

```bash
python main.py
```

Replace `main.py` with the name of your Python file if it is different.

## 🎯 Project Goal

This project is a practical exercise in computer vision, hand tracking, and gesture recognition. It demonstrates how hand movements can be used to interact with a computer without directly touching a keyboard or mouse.

## 🚀 Future Improvements

- Improve finger-counting accuracy.
- Add support for more hand gestures.
- Integrate system volume control.
- Improve gesture recognition under different lighting conditions.

## 👨‍💻 Author

Created as a Python programming course project.
