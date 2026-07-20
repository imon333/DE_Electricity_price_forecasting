"""
PowerCast - Price Forecasting Model
Predicts German day-ahead electricity price from weather and time features.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load the cleaned, merged dataset
df = pd.read_csv("data/processed/merged_2025.csv")
df["time"] = pd.to_datetime(df["time"])
df["month"] = df["time"].dt.month

# Features (inputs) and target (output)
X = df[["temperature_2m", "wind_speed_10m", "hour", "month"]]
y = df["price"]

# Split into train/test (80/20, reproducible with a fixed seed)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

# Compare against a naive baseline (always guessing the average price)
baseline_prediction = y_train.mean()
baseline_mae = mean_absolute_error(y_test, [baseline_prediction] * len(y_test))

if __name__ == "__main__":
    print("Model coefficients:", model.coef_)
    print("Model intercept:", model.intercept_)
    print(f"MAE: €{round(mae, 2)}")
    print(f"RMSE: €{round(rmse, 2)}")
    print(f"Baseline MAE: €{round(baseline_mae, 2)}")