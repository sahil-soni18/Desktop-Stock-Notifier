import time
import datetime
from plyer import notification
import yfinance as yf

# Create a ticker object for Google stock
google = yf.Ticker("GOOGL")

while True:
    # Fetch updated stock info
    googleInfo = google.info

    # Check if necessary keys are available in the info dictionary
    if 'currentPrice' in googleInfo and 'regularMarketDayLow' in googleInfo and 'regularMarketDayHigh' in googleInfo:
        try:
            notification.notify(
                title="Stock Price Alert".format(datetime.date.today()),
                message=f"Current Price: {googleInfo['currentPrice']},\n"
                        f"Day Low: {googleInfo['regularMarketDayLow']},\n"
                        f"Day High: {googleInfo['regularMarketDayHigh']}",

                timeout=10
            ) # type: ignore
        except Exception as e:
            print(f"Error occurred: {e}")
    else:
        print("Required stock information is not available.")

    # Delay before the next notification (e.g., 60 seconds)
    time.sleep(60*60*2)
