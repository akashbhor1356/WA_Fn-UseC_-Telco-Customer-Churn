from flask import Flask, request, jsonify
import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return "Customer Churn Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)
    
    # Convert the JSON data to a DataFrame
    df = pd.DataFrame([data])
    
    # Make a prediction
    prediction = model.predict(df)
    prediction_proba = model.predict_proba(df)[:, 1]
    
    # Return the result as JSON
    return jsonify({
        'prediction': int(prediction[0]),
        'prediction_proba': float(prediction_proba[0])
    })

if __name__ == '__main__':
    app.run(debug=True)
