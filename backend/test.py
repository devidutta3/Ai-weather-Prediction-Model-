from weather import get_weather
data=get_weather()

time=data["hourly"]["time"][0]
temp=data["hourly"]["temperature_2m"][0]
humidity=data["hourly"]["relative_humidity_2m"][0]
wind_speed=data["hourly"]["wind_speed_10m"][0]
soil_temp=data["hourly"]["soil_temperature_6cm"][0]

print(f"The Time :{time}")
print(f"The  Temperature:{temp}")
print(f"The  Humidity:{humidity}")
print(f"The  Wind Speed:{wind_speed}")
print(f"The  Soil Temperature:{soil_temp}")