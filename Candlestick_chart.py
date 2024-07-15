import yfinance as yahooFinance
import mplfinance as mpf
import pandas as pd

# Create a Ticker object for Meta
meta = yahooFinance.Ticker("NVDA")

# Fetch the last week's worth of data with a 1-minute interval
data = meta.history(period="5d", interval="60m")

# Rename the columns to match mplfinance expected format
data.rename(columns={"Open": "open", "High": "high", "Low": "low", "Close": "close", "Volume": "volume"}, inplace=True)

# Set the index to a DateTimeIndex if it's not already
data.index = pd.to_datetime(data.index)

# Plot the candlestick chart
mpf.plot(data, type='candle', style='charles', title='META Candlestick Chart - 1 Minute Interval', ylabel='Price', volume=True)
