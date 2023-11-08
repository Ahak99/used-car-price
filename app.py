from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictionPipeline


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods = ["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")
    else:
        data = CustomData(
            Location = request.form.get('Location'),
            Year = request.form.get('Year'),
            Kilometers_Driven = request.form.get('Kilometers_Driven'),
            Fuel_Type = request.form.get('Fuel_Type'),
            Transmission = request.form.get('Transmission'),
            Owner_Type = request.form.get('Owner_Type'),
            Mileage_kmpl = request.form.get('Mileage_kmpl'),
            Engine_CC = request.form.get('Engine_CC'),
            Power_bhp = request.form.get('Power_bhp'),
            Seats = request.form.get('Seats')
        )

        data_df = data.get_data_as_dataframe()
        print(data_df)

        predict_pipeline = PredictionPipeline()
        results = predict_pipeline.predict(data_df)

        return render_template('home.html', results = round(results[0], 2))
    

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)