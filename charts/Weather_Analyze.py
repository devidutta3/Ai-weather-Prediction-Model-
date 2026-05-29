import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data/Weather__data__.csv")

df["time"]=pd.to_datetime(df['time'])

plt.figure(figsize=(14,15))

plt.plot(df["time"],df["temperature"],color="red",linewidth=2,label="Temperature")
plt.plot(df["time"],df["humidity"],color="green",linewidth=1.5,label="Humidity")
plt.plot(df["time"],df["wind_speed"],color="blue",linewidth=2,label="Wind Speed")
plt.plot(df["time"],df["soil_temperature"],color="yellow",linewidth=2,label="Soil Temperature")
plt.legend()
plt.title("Temperature-Humidity-Wind Speed-Soil Temperature")
plt.xlabel("Time")
plt.ylabel("Value")

plt.legend()
plt.grid(True)

plt.show()