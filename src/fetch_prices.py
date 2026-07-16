import requests
import datetime
import pandas as pd

#get available timestamps
url = "https://www.smard.de/app/chart_data/4169/DE/index_hour.json"
response = requests.get(url)
data = response.json()


timestamps = data ["timestamps"]

readable_dates = [datetime.datetime.fromtimestamp(t/1000) for t in timestamps]


target = datetime.datetime(2025, 1, 1)
closest = min(readable_dates, key=lambda d: abs(d - target))
closest_index = readable_dates.index(closest)
chosen_timestamp = timestamps[closest_index]


print("starting from:", closest)

# get every timestamp from that point forward ---

remaining_timestamps = timestamps[closest_index:]
print("Numeber of weekly chuks to fetch:", len(remaining_timestamps))


all_row = []

for ts in remaining_timestamps:
    price_url = f"https://www.smard.de/app/chart_data/4169/DE/4169_DE_hour_{ts}.json"
    price_response = requests.get(price_url)
    price_data = price_response.json()
    week_series = price_data["series"]

    all_row.extend(week_series)

    # print("Fetched week starting:", datetime.datetime.fromtimestamp(ts / 1000), "- total rows so far:", len(all_row))

    last_time = datetime.datetime.fromtimestamp(week_series[-1][0] / 1000)
    if last_time > datetime.datetime(2026, 1, 1):
        break


print("Total hourly rows collected:", len(all_row))




 # turn the combined list into a DataFrame ----
df = pd.DataFrame(all_row, columns=["timestamp_ms", "price"])
df["time"] = pd.to_datetime(df["timestamp_ms"] / 1000, unit="s")

#   keep only rows within 2025 
df = df[(df["time"] >= "2025-01-01") & (df["time"] <= "2025-12-31 23:00:00")]


print(df.head())

 
# save to CSV 
df.to_csv("data/raw/prices_raw.csv", index=False)
print("Saved to data/raw/prices_raw.csv")

