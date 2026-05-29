import pandas as pd
from weather import get_weather

data=get_weather()

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"],
    "humidity": data["hourly"]["relative_humidity_2m"],
    "wind_speed": data["hourly"]["wind_speed_10m"],
    "soil_temperature": data["hourly"]["soil_temperature_6cm"]
})
df["time"] = pd.to_datetime(df["time"])

print(df.dtypes)
df.to_csv(r"C:\Users\dasde\OneDrive\Desktop\Ai-weather-Prediction-Model-\data\Weather__data__.csv",index=False)
print("CSV File Created Successfully :)")