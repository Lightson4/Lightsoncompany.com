import numpy as np
import pandas as pd
'''
student= {'Name': ["Nkechi", "ben", 'light', 'solo'], 
          'School':["FPO", "unizik", 'Igbariam', 'futo'],
          'Gender': ["Female", 'male', 'male', 'female'],
          "Dept": ['BAM', "PDM", 'MgT', "HRD"],
          "Level": ["ND2", "HND1", "ND1", "HND2"]}
Identity= pd.DataFrame(student)
print(Identity)
Identity.to_csv('Identity.csv', index=False)
RD = pd.read_csv('identity.csv')
print(RD)
#creating and reading Excel file in pandas
Identity.to_excel('Identity.xlsx', index=False)
RD1 = pd.read_excel('Identity.xlsx')
print(RD1)'''
#handling missing data
Handle = pd.DataFrame({
    'A': 
        [1,2,None, 4,5],
    "B":
        [1, 2, 3, 4, None]
})
print("Original Dataframe:")
print(Handle)
# forword fill in the missing values

Hd= Handle.fillna(method='ffill')
print("\nDataFrame after forward fill:")
print(Hd)
'''
churh = {"name": 
                ["light", "ferd", "blessing", "pp","confi"],
        "age": 
                [16, 43, 65, 87, 64],
        "personality": 
                    ["teacher", "gymer", "talor", "data", "student"]}
known=pd.DataFrame(churh)
print(known)
known.to_csv("known.csv", index= False)
CV = pd.read_csv('known.csv')
#grouping and aggregation
Company =pd.DataFrame ({"ID": ["hR", "It", "Customer care", "Fianace", "finder"],
             "salary": 
                    [40000, 50000, 32000, 75000, 30000,]})
grouping= Company.aggregate('salary').mean()
#print(grouping)
#advance...merging and joining
Company1 = pd.DataFrame({"ID": 
               
               ["solo", "ben", "light", "mary", "love"],
               
             "Gender": 
             
             ["male", "male", "male", "female" ,"female"]})

mergeers=pd.merge(Company, Company1, on="ID")
print(mergeers)
#pivotinged table
Busines=pd.DataFrame({"Date":
                      
                       ["4-10-01", "5-22-12", "6-09-11", "7-06-06"],
                      
                      "Sales":
                       
                        [5000, 2600, 6300, 9000],

                      "City":
                       
                        ["oko", "aba", "onisha", "owerri"]})
pivoted = Busines.pivot_table(values="Sales", index="Date", columns= "City", aggfunc= "sum")
print(pivoted)

#creat a pandas with columns and 6 rows filled with random intergers
df = pd.DataFrame(np.random.randint(1, 100, size=(6, 4)), columns=["A", "B", "C", "D" ])
print(df)
#set the index to be the first column
df.set_index("A", inplace=True)
print("Data with new index:")
print(df)

#class work
CDS = pd.DataFrame(np.random.randint(1, 100, size=(3, 3)), columns= ["A", "B", "C"], index=["X", "Y", "Z"])
#print("Original Dataframe:")
#print(CDS)
#Access the element at row "Y" and column "B"
Element = CDS.at['Z', 'C']
#print("Element at row 'Z' and column 'C':", Element)
#coover to csv_file
CDS.to_csv('CDS.cvs', index=False)
RD2= pd.read_csv('CDS.csv')
#print(RD2)
# to excell file
CDS.to_excel('CDS.xlsx', index= False)
RD3= pd.read_excel('CDS.xlsx')
#print(RD3)
#pandas dictionary with malty level indencing
Data= {
    ('coompanyA', 'IT'): [50000, 75000, 98000],
    ("companyA", 'HR'): [80000, 78000, 85000],
    ('coompanyB', 'IT'): [50000, 75000, 98000],
    ("companyB", 'HR'): [80000, 78000, 85000]
            
            
            }
Data1=pd.DataFrame(Data, index=['Year one', 'Year two', 'Year three'] )
print(Data1)

# dictionary with malty index framework
arrays = [
    ['CompanyA','CompanyA','CompanyB','CompanyB'],

    ['IT','HR','IT','HR']
]
index= pd.MultiIndex.from_arrays(arrays, names=('Company', 'Department'))
data = {
    'Salary':[50000, 80000,70000, 85000],
    'Employers': [10, 20, 15, 15]
}
multi= pd.DataFrame(data, index=index)
print(multi)
#dataframe with differcent date rangrs 
Wearther = {
    "Date":
         pd.date_range(start="2025- 02-01", periods = 7, freq= "D"),
    "Tempreture": 
        [10,20,30,40,50,60,70],
    "Humidity": 
        [30,40,50,60,70,80,90],
    "Space": np.random.choice(["30%","70%","78%", "50%", "90%"], size=7)
}
forecast = pd.DataFrame(Wearther, index= ["oko", "awka", "aba", "umuahia", "igbo", "eungu", "imo"])
print(forecast)'''