# ✋ Hand Gesture Control Project  

## 🚀 Abstract  
This project implements real-time hand gesture recognition using OpenCV, NumPy, and PyAutoGUI. It tracks hand movements through a webcam, detects convexity defects between fingers, and maps gestures to keyboard actions. Specifically, when an open-hand gesture (four or more defects) is detected, the system simulates a **spacebar press** which is good for controlling games or applications without physical input! pretty coool right??? 

---

## 🧠 Steps of Implementation  

### 1️⃣ Problem Definition  
Develop a real-time, **gesture-based control system** that replaces conventional input methods using hand movements.  

### 2️⃣ Hypothesis  
Hand shapes and finger positions can be tracked using **contours and convexity defects**, allowing gesture-based input control.  

### 3️⃣ Data Collection  
Video input is captured from a **webcam** and processed using OpenCV.  

### 4️⃣ Data Preprocessing  
- Convert the **Region of Interest (ROI)** to HSV color space.  
- Apply a **skin color mask** to isolate the hand.  
- Perform **thresholding** and **contour detection**.  

### 5️⃣ Gesture Recognition  
- Compute the **convex hull** and **convexity defects** of the hand contour.  
- If **four or more defects** are detected → **Simulate a spacebar press** using PyAutoGUI.  

### 6️⃣ Observation  
The system detects hand gestures with high accuracy in well-lit conditions and provides real-time feedback on recognized gestures.  

### 7️⃣ Conclusion  
The project successfully maps **hand gestures to keyboard inputs**, enabling a hands-free interaction method for various applications.  

---

## 📦 Installation  

To run this project, install the required dependencies:  

```bash
pip install opencv-python numpy pyautogui
```

---

## ▶️ Usage  

1. Run the script:  
   ```bash
   python hand_gestures.py
   ```  
2. **Show your hand inside the ROI** (displayed on screen).  
3. When **four or more fingers** are detected, the system **presses the spacebar** automatically.  
4. **Press "ESC" to exit.**  

---

## 🚀 Future Enhancements  

- Expand gesture controls to map additional actions (e.g., volume control, scrolling).  
- Improve robustness in **low-light conditions**.  
- Optimize hand segmentation for different **skin tones and backgrounds**.  

---

## 📜 License  

This project is open source and available under the [MIT License](LICENSE).  

---

Enjoy!!🤖✋
P.S. (If it doesn't work or theres a bug, I'll get back to this project I promise but rn its Feb, 20-tariff-25 and life be lifin so...) 
