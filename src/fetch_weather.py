import requests
import pandas as pd

url="https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": 53.55,
    "longitude": 9.99,
    "start_date": "2025-01-01",
    "end_date": "2025-12-31",
    "hourly": "temperature_2m,wind_speed_10m"
}

response = requests.get(url, params=params)
data = response.json()

print(data.keys())
print(data["hourly"].keys())

df = pd.DataFrame(data["hourly"])
print(df.head())
print(df.shape)


print(df.dtypes)
df["time"] = pd.to_datetime(df["time"])
print(df.dtypes)

df["hour"] = df["time"].dt.hour
print(df.head())
print(df.shape)

df.to_csv("data/raw/weather_raw.csv", index=False)
print("Saved to data/raw/weather_raw.csv")

