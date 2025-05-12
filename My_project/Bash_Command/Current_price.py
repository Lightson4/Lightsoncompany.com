import pandas as pd
import numpy as np
import yfinance as yf
#getting a live price in apple using the yahoo fianace API
apple = yf.Ticker('AAPL')

Current_price = apple.history(period = "1d")["Close"].iloc[-1] 

print(f"the Current price of apple: is ${Current_price:.2f}")

#creat a dataframe with historical prices for apple

df = apple.history(period="1y")

#print the first 5 row of the dataframe

print(df.head())
# calculate the avaerage prices for Apple over the year

aveverge_price = df["Close"].mean()

print(f"the average price over the year: is ${aveverge_price:.2f}")
#calacuating the minimum price for apple over the year
minimu_price = df["Close"].min()
print(f"the minimum price of the year: is ${minimu_price:.2f}")
# calculat the maximum of appple over the year

max_price = df["Close"].max()

print(f"the maximum price of apple over the year: is ${max_price:.2f}")

#calculate the minimum price of apple over the year
min_price = df["Close"].min()

print(f"the minimum price of apple over the year: is ${min_price:.2f}")

#calculate the standard deviation of apple's price over the yeaar
std_dev = df["Close"].std()

print(f" the standard deviation of apple over the year: is ${std_dev:.2f}")

print("Balance Sheet:")
print(apple.balance_sheet)
print("\nIncome statement:")
print(apple.financials)
print("\nCash flow statement:")
print(apple.cash_flow)