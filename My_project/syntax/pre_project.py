import pandas as pd



faculties = {
    "Engineering": ["Mechanical Engineering", "Civil Engineering", "Electrical Engineering"],
    "Science": ["Computer Science", "Biology", "Physics"],
    "Business": ["Accounting", "Marketing", "Business Administration"],
    "Arts": ["Mass Communication", "Theatre Arts", "English"],
    "Health": ["Nursing", "Medical Laboratory", "Pharmacy"]
}
project= {"Name":["Raymnd Ezeonyebuchi"],
         "Gender": ["Male"],
        "Age": 27,
        "facutly": ["financial studies"],
        "Department": ["insurance"],
        "Childhood course": ["Accountncy"],
        "Currently course": ["insurance"],
        "Are you Still studing your dream couse" : ["No"],
        "Reason" : ["I was given another course"],
        "Can you still ur dream course": ["Yes"],
        "Current course": ["Insuance"],
        "Satisfaction_level": ["Neutral"],
        "Do you mind priacting what you studies in real life": ["Yes"]
        }

df= pd.DataFrame(project)
print(df)
df.to_csv("df.csv", index=False)
pd.read_csv("df.csv")