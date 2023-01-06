import yfinance as yf
import pandas as pd

obj = yf.Ticker('BTC-USD')
obj.actions
dhr = yf.Ticker('DHR')
info = dhr.info
info.keys()
#above is just messing around 
#below is the code to get the data about crypto currencies
import requests
from requests_html import HTMLSession
session = HTMLSession()
num_currencies=250
headers = { 
    'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
    'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Language' : 'en-US,en;q=0.5',
    'DNT'             : '1', # Do Not Track Request Header 
    'Connection'      : 'close'
}
resp = session.get(f"https://finance.yahoo.com/crypto?offset=0&count={num_currencies}", headers=headers)
tables = pd.read_html(resp.html.raw_html)               
df = tables[0].copy()
symbols_yf = df.Symbol.tolist()
print(df.head(5))
tickers = symbols_yf[:25]
tickers = [yf.Ticker(ticker) for ticker in tickers]
max_type = ''
max_ratio = 0
# for ticker in tickers:
#     t_info = ticker.info
#     if (((t_info['fiftyTwoWeekHigh'] - t_info['fiftyTwoWeekLow']) / t_info['fiftyTwoWeekHigh']) > max_ratio):
#         max_ratio = ((t_info['fiftyTwoWeekHigh'] - t_info['fiftyTwoWeekLow']) / t_info['fiftyTwoWeekHigh'])
#         max_type = t_info['name']


print(type(df))
df.to_csv('stocks.csv')
