import yfinance as yf
import pandas as pd

# top 10 tickers from S&P 100
tickers = tickers = ["AAPL", "MSFT", "AMZN", "GOOGL", "NVDA", 
           "META", "TSLA", "JNJ", "JPM", "XOM"]

# download daily data (5 years)
data = yf.download(tickers, start="2018-01-01", end = "2025-01-01")["Adj Close"]

# save raw data
data.to_csv("data/raw/sp100_sample.csv")
print("Data saved to data/raw/sp100_sample.csv")
