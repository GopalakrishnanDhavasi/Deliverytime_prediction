# Deliverytime_prediction
Delivery_Time_Prediction
Here's a README file content for your Flask project with the delivery time prediction model:

---

# Delivery Time Prediction Web App

This is a Flask-based web application that predicts delivery time based on input features such as delivery person's age, rating, order type, vehicle type, and location coordinates. The app uses a trained Keras model along with preprocessing pipelines and scalers to generate accurate delivery time predictions.

## Features

* User inputs include:

  * Delivery person age (max 50)
  * Delivery person rating (max 6.0)
  * Order type (e.g., Snack, Meal)
  * Vehicle type (e.g., scooter, bike)
  * Restaurant and delivery location coordinates (latitude and longitude)

* Calculates the distance between restaurant and delivery locations using the spherical law of cosines.

* Applies preprocessing (scaling and encoding) before feeding the data to the ML model.

* Displays predicted delivery time after inverse transforming the scaled output.

## Requirements

* Python 3.7+
* Flask
* numpy
* pandas
* scikit-learn
* keras
* tensorflow
* joblib

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/delivery-time-predictor.git
   cd delivery-time-predictor
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have the following files in the project directory:

   * `model-final.h5` — trained Keras model
   * `preprocessing_pipeline.pkl` — preprocessing pipeline for input features
   * `target_scaler.pkl` — scaler for output target variable

5. Run the Flask app:

   ```bash
   python app.py
   ```

6. Open your web browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

## Usage

* Fill in the form with the required inputs.
* Submit the form to get the predicted delivery time.
* If inputs are invalid (e.g., age > 50 or rating > 6.0), an error message will be displayed.

## Notes

* Distance calculation uses the spherical law of cosines for more accurate geographical distance measurement.
* Input preprocessing includes feature scaling and one-hot encoding (implemented in `preprocessing_pipeline.pkl`).
* The model predicts scaled delivery times; output is inverse scaled before display.

## Troubleshooting

* Make sure all model and scaler files are present and compatible.
* If you encounter issues loading the model, verify your Keras and TensorFlow versions.
* For any other errors, check the console logs for details.

If you want, I can also help generate a `requirements.txt` based on your imports!

