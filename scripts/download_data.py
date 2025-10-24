import yfinance as yf
import pandas as pd
import os

os.makedirs("2025model_project/data/raw", exist_ok=True)

tickers = ["AAPL", "MSFT", "AMZN", "GOOG", "NVDA", 
           "META", "TSLA", "JNJ", "JPM", "XOM"]

all_data = {}

for ticker in tickers:
    print(f"Downloading {ticker}...")
    df = yf.download(ticker, start="2018-01-01", end="2025-01-01", auto_adjust=False)

    if df is not None and not df.empty:
        # Prefer "Adj Close", fallback to "Close"
        if "Adj Close" in df.columns:
            series = df["Adj Close"]
        elif "Close" in df.columns:
            series = df["Close"]
        else:
            print(f" No usable price column for {ticker}, skipping.")
            continue

        all_data[ticker] = series
        # Save each ticker separately
        series.to_csv(f"2025model_project/data/raw/{ticker}.csv")
        print(f" Saved {ticker} data to 2025model_project/data/raw/{ticker}.csv")

    else:
        print(f" No data for {ticker}, skipping.")

# Now you still have a dictionary of Series objects in memory
print("Finished downloading all tickers.")





data_dir = "data/raw"
tickers = ["AAPL", "MSFT", "AMZN", "GOOG", "NVDA",
           "META", "TSLA", "JNJ", "JPM", "XOM"]

all_series = []

for ticker in tickers:
    file_path = os.path.join(data_dir, f"{ticker}.csv")
    if os.path.exists(file_path):
        df = pd.read_csv(file_path, index_col=0, parse_dates=True)
        series = df[ticker].rename(ticker)  # enforce name
        all_series.append(series)
    else:
        print(f"Missing file for {ticker}, skipping.")

combined_df = pd.concat(all_series, axis=1)

os.makedirs("2025model_project/data/processed", exist_ok=True)
combined_df.to_csv("2025model_project/data/processed/prices.csv")

print("Combined dataset saved to data/processed/prices.csv")
print(combined_df.head())


