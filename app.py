from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load('model.lb')

# Map label integers to crop names using farmer.csv
df = pd.read_csv(r"C:\Final Project\Crop-Predictor\data\farmer.csv")
df['label'] = df['label'].astype('category')
label_map = dict(enumerate(df['label'].cat.categories))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project', methods=['GET', 'POST'])
def predict():
    crop = None  # Initialize crop
    if request.method == 'POST':
        # Collect inputs from form
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Predict
        input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        pred = model.predict(input_data)[0]

        # Convert label to crop name
        crop = label_map.get(pred, "Unknown Crop").capitalize()

    return render_template('project.html', crop=crop)

if __name__ == '__main__':
    app.run(debug=True)
