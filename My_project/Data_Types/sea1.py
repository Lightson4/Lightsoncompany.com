import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os 

data_df= pd.read_csv("data.csv")
data_df=(data_df.head(10))
print(data_df.info())
print(data_df.Sales)
print(data_df.Product)
x= data_df.Product
y= data_df.Sales
plt.xlabel("x=axis")
plt.ylabel("y=axis")
plt.scatter(x,y,color="black", marker="*")
plt.plot(x,y, color=("blue"))
plt.title("first assignment")
plt.show()

#second assignment

# Load the CSV file
df = pd.read_csv("data.csv")  # Update the file path if needed

# Check the first few rows to understand the data
print(df.head())

# Group by 'Region' and sum the 'Sales' column
region_sales = df.groupby('Region')['Sales'].sum()

# Find the region with the highest sales
max_region = region_sales.idxmax()
max_sales = region_sales.max()

# Plot a pie chart
plt.figure(figsize=(8, 6))
plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'lightcoral', 'gold'])
plt.title(f"Sales Distribution by Region (Highest: {max_region} - {max_sales})")
plt.show()


# Load the CSV file

df = pd.read_csv("data.csv")

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Drop rows with missing sales data
df_cleaned = df.dropna(subset=["Sales"])

# Sort by Date to analyze trends
df_cleaned = df_cleaned.sort_values(by="Date")

# Identify key sales points
highest_sales = df_cleaned["Sales"].max()
lowest_sales = df_cleaned["Sales"].min()
median_sales = df_cleaned["Sales"].median()

# Detect when sales started dropping
df_cleaned["Sales_Change"] = df_cleaned["Sales"].diff()
drop_start_date = df_cleaned.loc[df_cleaned["Sales_Change"] < 0, "Date"].min()

# Plot line chart for sales trend
plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="Sales", data=df_cleaned, marker="o", label="Sales")

# Highlight key points
plt.axhline(highest_sales, color="green", linestyle="--", label="Highest Sales")
plt.axhline(lowest_sales, color="red", linestyle="--", label="Lowest Sales")
plt.axhline(median_sales, color="blue", linestyle="--", label="Median Sales")

# Mark the drop start point
if pd.notna(drop_start_date):
    plt.axvline(drop_start_date, color="purple", linestyle="--", label="Sales Drop Start")

plt.legend()
plt.title("Sales Trend Analysis")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Plot bar chart for sales distribution
plt.figure(figsize=(12, 6))
sns.barplot(x="Date", y="Sales", data=df_cleaned, palette="viridis")

plt.title("Sales Distribution Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()
