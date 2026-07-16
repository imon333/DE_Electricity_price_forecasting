import pandas as pd

weather = pd.read_csv("data/raw/weather_raw.csv")
prices = pd.read_csv("data/raw/prices_raw.csv")

weather["time"] = pd.to_datetime(weather["time"])
prices["time"] = pd.to_datetime(prices["time"])

merged = pd.merge(weather, prices, on="time")
merged = merged.drop(columns=["timestamp_ms"])

merged.to_csv("data/processed/merged_2025.csv", index=False)
print("Saved to data/processed/merged_2025.csv")