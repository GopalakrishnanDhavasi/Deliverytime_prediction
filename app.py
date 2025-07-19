from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib
from keras.models import load_model

app = Flask(__name__)

# Load model and scalers
model = load_model("model-final.h5")
preprocessing_pipeline = joblib.load("preprocessing_pipeline.pkl")  # This includes one-hot and scaling
target_scaler = joblib.load("target_scaler.pkl")

# ✅ Spherical Law of Cosines function
def spherical_cosine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in km
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    return R * np.arccos(
        np.sin(lat1) * np.sin(lat2) +
        np.cos(lat1) * np.cos(lat2) * np.cos(lon2 - lon1)
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        try:
            # ✅ Get form inputs
            age = float(request.form['age'])
            rating = float(request.form['rating'])
            order_type = request.form['order']
            vehicle_type = request.form['vehicle']

            if age > 50:
                raise ValueError("Age must be 50 or below.")
            if rating > 6.0:
                raise ValueError("Rating must be 6.0 or below.")

            # ✅ Get lat/lon values from the form
            res_lat = float(request.form['restaurant_lat'])
            res_lon = float(request.form['restaurant_lon'])
            del_lat = float(request.form['delivery_lat'])
            del_lon = float(request.form['delivery_lon'])

            # ✅ Compute distance
            distance = spherical_cosine_distance(res_lat, res_lon, del_lat, del_lon)

            # ✅ Create input sample
            sample = pd.DataFrame([{
                'Delivery_person_Age': age,
                'Delivery_person_Ratings': rating,
                'distance': distance,
                'Type_of_order': order_type,
                'Type_of_vehicle': vehicle_type
            }])

            # ✅ Transform using pipeline
            input_scaled = preprocessing_pipeline.transform(sample)

            # ✅ Predict
            print(input_scaled)
            prediction_scaled = model.predict(input_scaled)
            prediction = target_scaler.inverse_transform(prediction_scaled)[0][0]
            prediction = round(prediction, 2)

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
