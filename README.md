Electric Motor Temperature Prediction Using Machine Learning
Project Overview

This project predicts the Permanent Magnet Surface (Rotor) Temperature of an electric motor using Machine Learning models and a Flask web application.

The system takes motor sensor inputs and predicts the rotor temperature for monitoring and predictive maintenance.

Technologies Used

Python

Pandas

NumPy

Scikit-learn

Flask

HTML & CSS

Machine Learning Workflow

Dataset collection from Kaggle

Data preprocessing

Exploratory Data Analysis (EDA)

Feature selection

Train-test split

Model training:

Linear Regression

Decision Tree

Random Forest (Best Model)

Model evaluation using:

R² Score

RMSE

Model saved using joblib

Flask deployment

Model Performance
Model	R² Score	RMSE
Linear Regression	0.60	11.98
Decision Tree	0.87	6.62
Random Forest	0.89	6.15

Random Forest performed best and is used for deployment.

Dataset

Dataset Name: PMSM Temperature Dataset
Source:
https://www.kaggle.com/datasets/wkirgsn/electric-motor-temperature

Note:
Due to GitHub file size limits, the dataset is not uploaded.
Download it from Kaggle and place it in the project root directory.

Project Structure

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

How to Run Locally

Open terminal

Go to Flask folder:

cd Flask

Install requirements:

pip install -r requirements.txt

Run app:

python app.py

Open browser:

http://127.0.0.1:5000

Use Case

This system can be used for:

Electric motor temperature monitoring

Predictive maintenance

Industrial motor health analysis

Deployment

This project can be deployed using:

Render

Railway

Heroku