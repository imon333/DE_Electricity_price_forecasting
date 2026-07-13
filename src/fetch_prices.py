import requests
import datetime

#get available timestamps
url = "https://www.smard.de/app/chart_data/4169/DE/index_hour.json"
response = requests.get(url)
data = response.json()

timestamps = data["timestamps"]

#find the timestamp closest to our target date
readable_dates = [datetime.datetime.fromtimestamp(t / 1000) for t in timestamps]
target = datetime.datetime(2025, 1, 1)
closest = min(readable_dates, key=lambda d: abs(d - target))
closest_index = readable_dates.index(closest)
chosen_timestamp = timestamps[closest_index]

print("Closest date:", closest)
print("Chosen timestamp:", chosen_timestamp)

# use that timestamp to fetch the actual price data
price_url = f"https://www.smard.de/app/chart_data/4169/DE/4169_DE_hour_{chosen_timestamp}.json"
price_response = requests.get(price_url)
price_data = price_response.json()

print(price_data.keys())