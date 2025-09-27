from flask import Flask, request, jsonify, send_from_directory # type: ignore
from flask_cors import CORS # type: ignore
import pickle
import numpy as np # type: ignore
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load model and scaler
model = pickle.load(open('regmodel.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))  # Save scaler as well in notebook

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([data['features']])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    return jsonify({'prediction': int(round(prediction[0]))})

@app.route('/')
def index():
    return send_from_directory('.', 'frontend.html')

@app.route('/frontend.html')
def frontend():
    return send_from_directory('.', 'frontend.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
