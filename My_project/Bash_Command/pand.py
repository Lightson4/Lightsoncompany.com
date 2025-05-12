import numpy as np
import pandas as pd
'''
#creatng a pandas series
data = [10,20,30,40,50]
series = pd.Series(data)
print(series)

data1 = ['lght', 'ben', 'solo','king', 'young']
series1 = pd.Series(data1)
print(series1)
(series[0:3])= 15,24, 10,
print(series1[1])
print(series1[4])
print(series)

#creating a data_frame from a dicitionary
data2 = {
    'name': ['Nelson', 'ben', 'solo'],
    'Age': [26, 20, 43], 
    'salary': [35000, 27000, 90000],
    'Gender': ['male', 'female', 'male'],
    "dept": ['HR', 'it', 'costomer']
    }
df = pd.DataFrame(data2)
#print(df)
# reading and writing data using pandas
df.to_csv('data2.csv', index= False)
RD = pd.read_csv("data2.csv")
print(RD)

#assingment
Numbers = pd.DataFrame(np.random.randint(1, 100, size=(3, 3)), columns=["A", "B", "C"], index=["X", "Y", "Z"])
#element extracting
Element = Numbers.at["Y", "B"]
print("element of row 'Y' and column 'B':", Element )
index = ({" "

})
#classwork
Data3 = {"Name": 
            ["Ben", "solo", "light"],
        "Age":
             [45, 76, 75],
    "Salary":
             [7000, 6000, 8000]}
#changing index to A B C
df =pd.DataFrame(Data3, index=["A", "B", "C"])
print(df)
#Dataframe with random data for sales analysis

Store= {"Date": 
                pd.date_range(start="2025-02-21", periods=10, freq= "D"),
        "Product": 
                np.random.choice(["rice", "beans", "spagetti", "planten", "cake", "garri", "mango", "bread", "tea", "gam"], size = 10),
        'Sales': 
                np.random.randint(10, 100, size=10),
        "Revenue":
                np.random.randint(1000, 10000, size=10)}
Store_Analy= pd.DataFrame(Store)
print(Store_Analy)'''
#stock market data using Yfinance
import yfinance as Yf
'''
#stock_data = Yf.download("AAPl", start="2024-01-01", end="2024-02-01")
#print(stock_data.head())

#fedefine stock tickers
tickers = ["AAPL", "MSFT", "TSLA"]
#DOWNLOADING STOCKDATA FROM YAHOO FINACEE
stock_data= Yf.download(tickers, start= "2024-01-01", end="2024-02-01")
#display the roll
print(stock_data)
df= stock_data.to_csv("stock_data.csv", index= False)
RD= pd.read_csv("stock_data.csv")
www= stock_data.to_html("stock_data.html", index=False)
#getting a live price in apple using the yahoo fianace API
apple = Yf.Ticker('AAPL')
Current_price = apple.history(period = "2d")["Close"].iloc[-2] 
print(f"the Current price of apple: is ${Current_price:.2f}")
'''
'''
RD= pd.read_csv("data.csv")
print(RD.head(10))
print(RD.tail(5))
print(RD["Value"])
print(RD["Date"])
#print(RD.head(10)["Sales"])
#print(RD.tail(10)["Sales"])
#print(RD.at[30, "Sales"])
#print(RD["Date"])
print(RD.at[20, "Date"], RD.at[20,"Sales"], RD.at[10,"Value"], RD.at[10,"Product"])
print(RD.iat[5, 4], RD.iat[24, 3])
print(RD.iat[8, 0], RD.iat[8, 1], RD.iat[8, 2], RD.iat[8, 4])
#how to add a column 

RD["City"]=np.random.choice(["aba", "umuahia", "awka", "oko"], size=50)
rd=RD.to_csv("data.csv", index=False)
#how delet a column
RD.drop("Cities", axis=1, inplace=True)
rd=RD.to_csv("data.csv", index=False)
#Number= pd.DataFrame(np.random.randint(1,100, index=["a", "b", "c",], size=(6, 6),))

RD["Product"]=np.random.choice(['Iphone', 'infinix', 'itel', 'redmi'], size=50)
rd=RD.to_csv("data.csv",index=False)
#******** how to delete a column*************
RD.drop("Products", axis=1, inplace=True)
rd=RD.to_csv("data.csv", index=False)
#renaming columns 
RD= RD.rename(columns={"Date": 'Date Sales'})
print(RD.tail(21))
RD=RD.rename(columns={"Sales": "Purchase", "Value": "Rate", "Product": "Servies"})
print(RD.head(20))
#grouping sum
group_sum= RD.groupby(["Servies", "Region"])["Rate"].sum(),RD.groupby(["Servies", "Region"])["Purchase"].sum()
print(group_sum)

group_mean= RD.groupby(["Servies", "Region"])["Rate"].mean(),RD.groupby(["Servies", "Region"])["Purchase"].mean()
print(group_mean)
group_agg= RD.groupby(["Servies", "Region"])["Rate"].agg(["mean", "sum", "count"])
print(group_agg)
#group_sum1= RD.groupby(["Servies", "Region"])["Purchase"].sum()
#print(group_sum1)
'''
