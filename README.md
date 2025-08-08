# 🌾 Crop Recommendation System

A machine learning-powered web application that predicts the most suitable crop to grow based on environmental and soil parameters such as nitrogen (N), phosphorus (P), potassium (K), temperature, humidity, pH, and rainfall.

---

## 🌐 View Online

🌱 Live Demo: https://sakshamsharma-code.github.io/Crop-Predictor/

---

## 🔍 Overview

This system helps farmers and agriculturists make informed decisions by suggesting the optimal crop to cultivate based on the current conditions. It leverages a Random Forest classifier trained on historical agricultural data.

---

## 🎯 Features

- ✅ Input-based crop recommendation
- ✅ Interactive HTML frontend (deployed via GitHub Pages)
- ✅ Flask backend with ML prediction
- ✅ Minimal, clean Bootstrap UI

---

## 🗂 Project Structure
```
Crop-Predictor/
├── app.py # Flask backend
├── model.lb # Trained ML model (RandomForest)
├── data/
│ └── farmer.csv # Original dataset
│ └── Cleaned_farmer.csv # Cleaned dataset
├── templates/
│ ├── index.html # Home page
│ ├── project.html # Crop recommendation form
│ ├── about.html # About page
│ └── contact.html # Contact page
├── static/ # images
└── README.md
```
---

## ⚙️ Technologies Used

- Python
- Flask
- scikit-learn
- Pandas & NumPy
- HTML, CSS (Bootstrap 5)

---

## 📊 Model Training

- Algorithm: RandomForestClassifier
- Accuracy: ~99% on test set
- Preprocessing: Label Encoding
- Output: Integer labels mapped to crop names

---

## 🧪 How to Run Locally

1. Clone the repository:

```bash
git clone 
cd Crop-Predictor
```
Install required packages:

```bash
pip install -r requirements.txt
```

Start the Flask server:
```bash
python app.py
```

Open your browser and navigate to:
```cpp
http://127.0.0.1:5000/
```

---

## 👨‍💻 Author
Developed by Saksham Sharma
