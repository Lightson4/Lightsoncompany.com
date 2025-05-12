import pandas as pd
import numpy as np
#NO 1
'''
ass = pd.DataFrame(np.random.randint(1, 100, size=(4, 6)))
print(ass)
#NO 2
ass1 = pd.DataFrame(np.random.randint(1, 100, size=(3, 3)), columns=["A", "B", "C"], index=["X", "Y", "Z"])
print(f"ass1:", ass1)
#accessing the row element
Access = ass1.at["Y", "B"]
print("access of row 'Y' and column 'B':", Access )
#NO 3
ass2 = pd.DataFrame(np.random.randint(1, 100, size=(5,3)), columns=["A", "B", "C"])
print(ass2)

#NO 4
ass3 = pd.DataFrame(np.random.randint(1, 100, size=(4, 3)), columns=["A", "B", "C"])
#compute the row-wise count
row_sum = ass3.sum(axis=1)
#compute the column-wie
column_sum = ass3.sum(axis=0)
print("original dataframe:")
print(ass3)
print("\nrow-wise sum:")
print(row_sum)
print("\nColumn-wise sum:")
print(column_sum)
#NO 5
ass4 = pd.DataFrame(np.random.randint(1, 100, size=(3,5)), columns=["A", "B", "C"])
ass4.loc[0, "A"] = np.nan
ass4.loc[1, "B"] = np.nan
ass4.loc[2, "c"] = np.nan
print("original Dataframe with NaN values:")
print(ass4)
#fill nan value the mean of the respective columns
ass4_filled = ass4.fillna(ass4.mean())
print("\ndataframe with nan value filled with mean:")
print(ass4_filled)
#no 6
ass5 = pd.DataFrame(np.random.randint(1, 100, size=(6,4)), columns=["A", "B", "C", "D"])
ass5.loc[1, "B"]= np.nan
ass5.loc[3, "C"]= np.nan
ass5.loc[5, "D"]= np.nan
print("original Dataframe with NaN values:")
print(ass5)
#drop rows with any nan valuse 
ass5_droped = ass5.drop()
print("\nDataframe with rows containing nan valuse dropped:")
print(ass5_droped)
#no 7 
ass6 = pd.DataFrame({"Category": 
             np.random.random("A", "B", "C"),
        "value": 
        np.random.randint()})

#no 8
# Create a Pandas DataFrame with 2 columns: 'Category' and 'Value'
ass7 = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=10),
    'Value': np.random.randint(1, 100, size=10)})
print("Original DataFrame:")
print(ass7)
# Group the DataFrame by 'Category' and compute the sum and mean of 'Value' for each category
grouped_ass7 = ass7.groupby('Category')['Value'].agg(['sum', 'mean'])

print("\nGrouped DataFrame:")
print(grouped_ass7)
 '''
 #no 9

 # Create a Pandas DataFrame with 3 columns: 'Product', 'Category', and 'Sales'
df = pd.DataFrame({
    'Product': np.random.choice(['Iphone', 'infinix', 'itel', 'redmi'], size=10),
    'Category': np.random.choice(['Category 1', 'Category 2', 'Category 3'], size=10),
    'Sales': np.random.randint(1, 100, size=10)
})

print("Original DataFrame:")
print(df)
'''
# Group the DataFrame by 'Category' and compute the total sales for each category
category_sales = df.groupby('Category')['Sales'].sum().reset_index()

print("\nTotal Sales by Category:")
print(category_sales)

#10
#1. Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers. Set the index to be the first column.

ass8 = pd.DataFrame(np.random.randint(1, 100, size=(6,4)),columns=["A","B", "C", "D" ])
ass8.set_index("A", inplace=True)
print(ass8)


#no 11
# Create a Pandas DataFrame with a datetime index and one column filled with random integers
start_date = '2022-01-01'
end_date = '2022-12-31'
date_index = pd.date_range(start=start_date, end=end_date)
df = pd.DataFrame(np.random.randint(1, 100, size=len(date_index)), index=date_index, columns=['Values'])

print("Original DataFrame:")
print(df.head())

# Resample the DataFrame to compute the monthly mean of the values
monthly_mean = df.resample('M').mean()

print("\nMonthly Mean:")
print(monthly_mean)

date_index = pd.date_range(start="2022-01-01", end="2022-12-31")
df = pd.DataFrame(np.random.randint(1, 100, size=len(date_index)), index=date_index, columns=["Values"])

monthly_mean = df.resample('M').mean()

print("\nMonthly Mean:")
print(monthly_mean)


#no 9
#applying functions and lamda function
arre = pd.DataFrame(np.random.randint(1, 100, size=(3,5)))
double = arre **2
print(double)
double = lambda x:x *2
print(double(10))

#no 8 
#creatingg of a pivoted table to compute the sum for "value" for each "category" by "Date" 

pivot_table = df.pivot_table(values="value", index="Date", columns="Category", aggfunc="sum")
print("pivot_table:")
print(pivot_table)

#create a pandas Dataframe with colums "years", "Quarter", and "Revenue"
df= pd.DataFrame({"Years":
                  np.random.choice([2020, 2021,2022], size=12),
                  "Quarter": np.random.choice(["Q1", "Q2", "Q3", "Q4"], size=12),
                  "Revenue": np.random.randint(1, 1000, size=(12))
                  })
print("Original Dataframe:")
print(df)
#create a pivot table to compute the mean "Revenun", for eac "Quarter", and " Revenun"
pivot_table = df.pivot_table(values="Revenue", index="Years", columns="Quarter", aggfunc="mean")
print(f"pivot_table:", pivot_table)



# no 19
# Create a Pandas Series with 5 random text strings
series = pd.Series(['hello', 'world', 'python', 'pandas', 'numpy'])

# Convert all the strings to uppercase
uppercase_series = series.str.upper()

print(uppercase_series)


#20
# Create a Pandas Series with 5 random text strings
series = pd.Series(['hello', 'world', 'python', 'pandas', 'numpy'])

# Extract the first three characters of each string
first_three_chars = series.str[:3]

print(first_three_chars)
'''