
# <img src="https://github.com/MohammedKaif-3/Liver_Cirrhosis/blob/main/Flask/static/assets/favicon.png" height=50 /> HepaCheck – Revolutionising Liver Care | Liver Cirrhosis Prediction System

**HepaCheck** is a lightweight, responsive AI-powered web application that predicts the risk of liver cirrhosis based on clinical parameters. Designed to assist healthcare professionals and researchers in early-stage detection, it combines machine learning with a simple user interface for quick predictions and interpretability.

---

## 🚀 Live Demo
👉 [Click to Try HepaCheck](https://hepacheck.pythonanywhere.com)

---

## 📽️ Demo Video
🎥 [Watch the Demo on Google Drive](https://drive.google.com/file/d/1r0yT9LP-eMFMNDLHWC5uexgbeYyShtvl/view?usp=sharing)

---

## 🧪 Features

- 🔍 Predicts cirrhosis risk from 20+ clinical inputs
- 📊 Visualizes feature importance using Chart.js
- 🧠 Trained Random Forest model.
- ✅ Real-time prediction with color-coded feedback
- 📱 Fully responsive and mobile-friendly UI
- 🧪 Auto-fill demo button for quick testing

---

## 📂 Project Structure

```
Liver_Cirrhosis/
│
├── Flask/                          # Main application folder
│   │
│   ├── static/                     # Static assets
│   │   ├── main.js
│   │   ├── stylesheets/
│   │   │   ├── base.css
│   │   │   ├── index.css
│   │   │   ├── predict.css
│   │   │   └── results.css
│   │   └── assets/                # Logos, icons, etc.
│   │
│   ├── templates/                 # Jinja2 HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── predict.html
│   │   └── results.html
│   │
│   ├──normalizer.pkl                  # Trained ML models (optional structure)
│   ├── rf_acc_68.pkl
│   │
│   │
│   ├── app.py                     # Flask backend
│   └── requirements.txt           # Python dependencies
│
├── Training/                      # Model development notebook
│   └── Liver_cirrhosis.ipynb
│
├── Documentation/                # Reports and media
│   ├── HepaCheck_Presentation.pptx
|   ├── Research_Report.pdf
│   ├── Demo.mp4
│   └── Project_Report.pdf
│
├── Data/                   
│     └── liver_dataset.xlsx
└── README.md                      # Project documentation
```

---

## 🧬 Machine Learning Model

- **Dataset**: [Kaggle Liver Cirrhosis Dataset](https://www.kaggle.com/datasets/bhavanipriya222/liver-cirrhosis-prediction)
- **Algorithms Tried**: Logistic Regression, Decision Trees, SVM, Random Forest
- **Final Model**: Random Forest (GridSearchCV tuned)
- **Preprocessing**: Handling nulls, feature scaling, SMOTE resampling

---

## 🛠️ Tech Stack

| Layer      | Technology            |
|------------|------------------------|
| Frontend   | HTML, CSS, JS          |
| Backend    | Flask (Python)         |
| ML         | Scikit-learn           |
| Visuals    | Chart.js               |
| Hosting    | PythonAnywhere         |


## Author
- Mohammed Kaif

---

## 📌 How to Run Locally

```bash
git clone https://github.com/MohammedKaif-3/Liver_Cirrhosis.git
cd Liver_Cirrhosis
pip install -r requirements.txt
python app.py
```

---
