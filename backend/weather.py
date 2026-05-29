import requests as r

def get_weather():

    url="https://api.open-meteo.com/v1/forecast?latitude=20.2724&longitude=85.8338&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m,soil_temperature_6cm"
    response=r.get(url)

    return response.json()


