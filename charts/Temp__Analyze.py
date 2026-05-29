import pandas as pd
import  matplotlib.pyplot as plt 

df=pd.read_csv("data/Weather__data__.csv")
print(df["temperature"].max())
print(df["temperature"].min())
df["time"]=pd.to_datetime(df["time"])
plt.figure(figsize=(10,5))

plt.plot(df["time"],df["temperature"],color="red",linewidth=2)
plt.title("Temperature Crisis")
plt.xlabel("Time")
plt.ylabel("Temperature In (°C)")
plt.grid(True)
plt.show()
print(df.describe())