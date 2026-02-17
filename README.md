# 🚀 Electric Motor Temperature Prediction Using Machine Learning

## 📌 Project Overview

This project predicts the **Permanent Magnet Surface (Rotor) Temperature** of an electric motor using Machine Learning models and a Flask web application.

The system takes motor sensor inputs and predicts the rotor temperature for monitoring and predictive maintenance.

---

## 🛠 Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Flask  
- HTML & CSS  

---

## 🤖 Machine Learning Workflow

1. Dataset collection from Kaggle  
2. Data preprocessing  
3. Exploratory Data Analysis (EDA)  
4. Feature selection  
5. Train-test split  
6. Model training:
   - Linear Regression
   - Decision Tree
   - Random Forest (Best Model)
7. Model evaluation using:
   - R² Score
   - RMSE
8. Model saved using `joblib`
9. Flask deployment  

---

## 📊 Model Performance

| Model              | R² Score | RMSE  |
|--------------------|----------|-------|
| Linear Regression  | 0.60     | 11.98 |
| Decision Tree      | 0.87     | 6.62  |
| Random Forest      | 0.89     | 6.15  |

✅ **Random Forest performed best and is used for deployment.**

---

## 📂 Dataset

- **Dataset Name:** PMSM Temperature Dataset  
- **Source:**  
  https://www.kaggle.com/datasets/wkirgsn/electric-motor-temperature  

> ⚠ Due to GitHub file size limits, the dataset is not uploaded.  
> Download it from Kaggle and place it in the project root directory.

---

## 📁 Project Structure
Electric_Motor_Temperature_Project
│
├── Flask/
│ ├── app.py
│ ├── Procfile
│ ├── requirements.txt
│ └── templates/
│ ├── index.html
│ └── manual_predict.html
│
├── model.save
├── transform.save
└── README.md


---

## ▶️ How to Run Locally

1️⃣ Open terminal  

2️⃣ Go to Flask folder:

cd Flask

3️⃣ Install requirements:
pip install -r requirements.txt

4️⃣ Run the application:
python app.py

5️⃣ Open browser:
http://127.0.0.1:5000

🎯 Use Case

This system can be used for:
Electric motor temperature monitoring
Predictive maintenance
Industrial motor health analysis


## 🌐 Live Demo
https://electric-motor-temperature-prediction-1-2lnd.onrender.com/

DEMO VIDEO:
https://drive.google.com/file/d/1Ltb4HvUFvx7EeXuZF0C9c90869jsBTlm/view?usp=sharing


