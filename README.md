# Customer Churn Prediction

## Overview
This project predicts customer churn for a telecom company using a machine learning model.

## Steps to Run

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-repo/churn-prediction.git
    cd churn-prediction
    ```

2. **Build and run the Docker container**:
    ```sh
    docker build -t churn-prediction .
    docker run -p 5000:5000 churn-prediction
    ```

3. **Make a prediction**:
    Send a POST request to `http://localhost:5000/predict` with customer data.

## Data
The dataset used is [Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn).

## Model
A Random Forest model is trained to predict churn.

## API
The Flask app provides a REST API to make predictions.
