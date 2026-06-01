from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = Path(__file__).resolve().parent.parent / "models" / "weather_model.pkl"
with open(model_path, "rb") as file:
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