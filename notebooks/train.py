import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/Weather__data__.csv")

X = df[
    [
        "humidity",
        "wind_speed",
        "soil_temperature"
    ]
]

y = df["temperature"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

with open("models/weather_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Saved Successfully!")