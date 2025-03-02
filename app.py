from flask import Flask, request, jsonify, render_template, send_from_directory
import shap
import os
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# Load the trained model and scaler
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Define feature columns
feature_columns = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 
                   'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope']

# Directory to save SHAP plots
SHAP_PLOT_DIR = 'shap_plots'
if not os.path.exists(SHAP_PLOT_DIR):
    os.makedirs(SHAP_PLOT_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Ensure all required features exist in the input JSON
        if not all(feature in data for feature in feature_columns):
            return jsonify({"error": "Missing required features in input JSON"}), 400

        # Convert input to DataFrame and order columns properly
        input_data = pd.DataFrame([data])[feature_columns]

        # Scale the input data
        input_data_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_data_scaled)[0]
        prediction_proba = model.predict_proba(input_data_scaled)[0, 1]

        # Convert prediction to readable labels
        prediction_label = "Heart Disease" if prediction == 1 else "No Heart Disease"

        # SHAP explanation
        explainer = shap.Explainer(model, input_data_scaled)
        shap_values = explainer(input_data_scaled)

        # 🔹 Extract SHAP values for class 1 (Heart Disease) 🔹
        if isinstance(shap_values, shap.Explanation):
            shap_values_array = shap_values.values[:,:,1]  # Focus on class 1
        else:
            shap_values_array = shap_values[:,:,1]

        # Get top 3 influential features
        feature_importance = np.abs(shap_values_array).mean(axis=0)  # Mean importance
        top_features_idx = np.argsort(feature_importance)[-3:][::-1]  # Top 3 features
        top_features = [feature_columns[i] for i in top_features_idx]

        # Save SHAP plot
        shap_plot_path = os.path.join(SHAP_PLOT_DIR, 'shap_summary_plot.png')
        shap.summary_plot(shap_values, input_data, show=False)
        plt.savefig(shap_plot_path, bbox_inches="tight")
        plt.close()

        return jsonify({
            'prediction': prediction_label,
            'prediction_probability': float(prediction_proba),
            'top_influential_features': top_features,
            'shap_plot_url': f'/shap_plots/shap_summary_plot.png'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/shap_plots/<filename>')
def serve_shap_plot(filename):
    return send_from_directory(SHAP_PLOT_DIR, filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
