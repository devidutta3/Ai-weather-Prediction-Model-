import pickle

with open("models/weather_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)
print(type(loaded_model))