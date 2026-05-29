from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

with open("models/weather_model.pkl", "rb") as file:
    model = pickle.load(file)

class WeatherInput(BaseModel):
    humidity: float
    wind_speed: float
    soil_temperature: float

@app.get("/")
def home():
    return {
        "message": "AI Weather Dashboard API Running Successfully!"
    }

@app.post("/predict")
def predict(data: WeatherInput):

    input_data = pd.DataFrame([{
        "humidity": data.humidity,
        "wind_speed": data.wind_speed,
        "soil_temperature": data.soil_temperature
    }])

    prediction = model.predict(input_data)

    return {
        "predicted_temperature": float(prediction[0])
    }