import visualization as vs
#print(vs.df.Gender.to_csv('gender.csv', index= True))

#print(vs.df['Gender'].unique())

vs.df['Gender'] = vs.df['Gender'].astype(str).str.strip().str.lower()

# Map common variations
vs.df['Gender'] = vs.df['Gender'].replace({
    'm': 'male',
    'f': 'female',
    'male': 'Male',
    'female': 'Female'
})
gender_counts= vs.df["Gender"].value_counts()
print(gender_counts)

'''
vs.plt.figure(figsize=(7, 7))
vs.df["Gender"].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=["skyblue", "pink"], startangle=90)
vs.plt.title("Gender Distribution")
vs.plt.ylabel("")  # Hides the y-label for better display
vs.plt.show()


data_df= pd.read_csv("data.csv")
data_df=(data_df.head(10))
print(data_df.info())
print(data_df.Sales)
print(data_df.Product)
x= data_df.Product
y= data_df.Sales'
'''