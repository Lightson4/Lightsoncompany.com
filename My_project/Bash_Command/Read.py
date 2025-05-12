import pandas as pd
from io import StringIO
import json 
import numpy as np

'''
Data = '{"employee_names": "Nelson", "Egmail": "nelsonlight684@gmail.com", "Job_Profile": [{"title1":"Data Analysis", "title2": "HR"}]}'
df=pd.read_json(StringIO(Data))
print(df)

# Create a Pandas DataFrame
Data = {
    "Employee names": ["Nelson Blessing", "Benjamin Thankgod", "Solomon Arate", "Favour Christopher", "Mctim Timothy"],
    "Egmail": ["nelsonlight684@gmail.com", "Benjaminthankgod@gmail.com", "solomonareate@gmail.com", "chiamaka@gmail.com", "viviana@gmail.com"],
    "Job Profile": [["Data analysis"], ["HR", "IT"], ["OPENER"], ["Costomer care"], ["Cashier"]],
    "Gender" : ["Male", "Male", "Male", "Female", "Female"],
    "Age": [45, 78, 98, 12, 37],
    "City": ["ABA", "OKo", "Ndika", "Awka", "owerri"], 
    "Marritail Status": ["Single", "Married", "Single", "Single", "Maarried"]

}
df = pd.DataFrame(Data)
print(df)

# Convert the DataFrame to a JSON string
#json_str = df.to_json(orient='records')

# Read the JSON string into a new DataFrame
#new_df = pd.read_json(StringIO(json_str))

Data = pd.read_csv("http://archive.ics.mtn.edu/ml/machine-learning-databases/wine/wine.data", header=None)
print(Data.tail)

url= "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"
data = pd.read_html(url)
print(data)
'''
url1="https://en.wikipedia.org/wiki/Mobile_country_code"
pd.read_html(url1,match="Country",header=0)[0]
Data = pd.read_html(url1)
print (Data)
