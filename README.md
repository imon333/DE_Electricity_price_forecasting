# PowerCast

Forecasting German day-ahead electricity prices using weather data.

## Why

Electricity prices in Germany are heavily influenced by renewable generation —
wind and solar output depend directly on weather conditions, and demand shifts
with temperature (heating/cooling). This project explores whether weather data
(temperature, wind speed) can help explain and forecast electricity price
movements, using real historical data.

## Data Sources

- **[Open-Meteo](https://open-meteo.com/)** — free historical weather data (temperature, wind speed), no API key required
- **[SMARD](https://www.smard.de/)** — free German electricity market data (day-ahead prices), provided by the Bundesnetzagentur, no API key required

## Key Findings

- Wind speed and price: **-0.39 correlation** — higher wind, lower price, consistent with the merit order effect (cheap renewable supply displacing expensive fossil generation)
- Temperature and price: **-0.33 correlation** — likely reflecting Germany's winter heating-driven demand
- Negative prices occurred in a meaningful share of hours in 2025, clustering in spring/summer months, consistent with solar oversupply
- Most expensive hour: **€583.40** (Jan 20, 16:00 — cold, low wind, high heating demand)
- Cheapest hour: **-€250.32** (May 11, 11:00 — warm, moderate wind, midday solar peak, low demand)

## Model

Linear Regression predicting price from temperature, wind speed, hour, and month.

| Metric | Value |
|---|---|
| MAE | €31.63 |
| RMSE | €45.73 |
| Baseline MAE (naive average) | €35.95 |

The model outperforms a naive baseline (always guessing the average price), confirming
weather and time features add real predictive value — though the modest margin shows
electricity price is driven by many additional factors (demand shifts, gas prices, grid
conditions) not captured by this simple model.

## Project Structure

```text
DE_Electricity_price_forecasting/
├── data/
│   ├── raw/              # untouched data straight from APIs
│   └── processed/        # cleaned, merged data
├── notebooks/            # exploration, EDA, quick experiments
├── src/                  # reusable functions — the "real" code
│   ├── fetch_weather.py
│   ├── fetch_prices.py
│   ├── clean_data.py
│   └── model.py
├── outputs/
│   └── figures/          # saved charts
├── requirements.txt
├── README.md
└── .gitignore
```

## Tech Stack

Python, pandas, NumPy, requests, matplotlib, scikit-learn

## Status

Complete — data pipeline, EDA, and baseline forecasting model built and evaluated.