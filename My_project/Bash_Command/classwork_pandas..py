import numpy as np
import pandas as pd

'''Date_rng = pd.date_range(start= '2024-01-01', end= '2024-12-31', freq= 'D')
df =pd.DataFrame(Date_rng, columns=["date"])
df["data"] = np.random.randint(0, 100, size=(len(Date_rng)))
df.set_index("date", inplace=True)
print("Original dateFrame:")
#print(df)
rolling_mean= df.rolling(window=7).mean()
print(rolling_mean)

#another classwork
Numbers = pd.DataFrame(np.random.randint(1, 100, size=(3, 5)))
Light = pd.DataFrame(np.random.randint(0, 100, size=(5, 5)))
print(F"Light:", Light)
double = Light **2
print(f"double", double)
#print(Numbers)
double = Numbers **2
#print(double)

#another
data = (["hello", "world", "python", "pandas", "numpy"])
series = pd.Series(data)
#converting to upper case
series_upper = series.str.upper()''
#print(series_upper)
ass8 = pd.DataFrame(np.random.randint(1, 100, size=(6,4)),columns=["A","B", "C", "D" ])
ass8.set_index("A", inplace=True)
print(ass8)'''

date_index = pd.date_range(start="2022-01-01", end="2022-12-31")
df = pd.DataFrame(np.random.randint(1, 100, size=len(date_index)), index=(date_index), columns=["Values"])

monthly_mean = df.resample('M').mean()

print("\nMonthly Mean:")
print(monthly_mean)
