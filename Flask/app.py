from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.save")
scaler = joblib.load("transform.save")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict')
def predict_page():
    return render_template('manual_predict.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = scaler.transform([features])
    prediction = model.predict(final_features)

    return render_template('manual_predict.html',
                           prediction_text=f"Predicted Rotor Temperature: {prediction[0]:.2f}")
    
if __name__ == "__main__":
    app.run(debug=True)
