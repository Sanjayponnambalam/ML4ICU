import os
import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='website/templates')

# Specify the folder path (where the model and scaler are saved)
model_path = '../patient_deterioration_model.pkl'
scaler_path = '../scaler.pkl'
# Load the saved model using pickle
with open(model_path, 'rb') as f:
    bagging_model = pickle.load(f)

# Load the scaler using pickle
with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data (sent as JSON)
    data = request.get_json()

    # Extract the parameters from the JSON data
    heart_rate = float(data['Heart_Rate'])
    respiratory_rate = float(data['Respiratory_Rate'])
    body_temperature = float(data['Body_Temperature'])
    oxygen_saturation = float(data['Oxygen_Saturation'])
    derived_hrv = float(data['Derived_HRV'])
    derived_bmi = float(data['Derived_BMI'])
    derived_map = float(data['Derived_MAP'])

    # Prepare the input data as a numpy array
    input_data = np.array([[heart_rate, respiratory_rate, body_temperature,
                            oxygen_saturation, derived_hrv, derived_bmi, derived_map]])

    # Scale the input data using the saved scaler
    scaled_data = scaler.transform(input_data)

    # Make the prediction using the loaded model
    prediction = bagging_model.predict(scaled_data)

    # Return the prediction result as JSON
    return jsonify({'prediction': 'High Risk' if prediction[0] == 0 else 'Low Risk'})

if __name__ == "__main__":
    app.run(debug=True)
