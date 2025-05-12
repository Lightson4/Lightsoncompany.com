#Python Implementation

#1. Generate Synthetic Data and Save to CSV

import pandas as pd
import random
import numpy as np


# Sample faculties and departments
faculties = {
    "Engineering": ["Mechanical Engineering", "Civil Engineering", "Electrical Engineering"],
    "Science": ["Computer Science", "Biology", "Physics"],
    "Business": ["Accounting", "Marketing", "Business Administration"],
    "Arts": ["Mass Communication", "Theatre Arts", "English"],
    "Health": ["Nursing", "Medical Laboratory", "Pharmacy"]
}

# Sample childhood dream courses
dream_courses = ["Medicine", "Law", "Engineering", "Computer Science", "Accounting", "Nursing", "Architecture"]

# Sample reasons for not studying dream course
reasons = ["Financial constraints", "Didn't meet admission requirements", "Parental influence", "Changed interest", "Course was not available"]

# Satisfaction levels
satisfaction_levels = ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"]

# Generate random student data
students = []
for i in range(200):

#arre =np.random.randint(1, 200, size=(freq=200))
    full_name =random.choice(["Victor Light", "Mercy Chibuchi", "Mctim Timothy", "Grace Goodness", "Excel justice", "Miracle Okeoma", "Monday Stanley", "France Prince", "Solomon Benjemin", "Uche  Smart", "Victor Light", "Eman Bliss", "Victor Light", "Pleasure Gift", "Victor Light", "Eman Bliss", "Victor Light", "Eman Bliss", "Precious Alison", "Ibe Okeugo", 
"Blessing Nelson", "Ochor Friday", "Victoria Frank", "Divine Favour", "Fortune Ezeane"])
    gender = random.choice(["Male", "Female"])
    age = random.randint(17, 30)
    faculty = random.choice(list(faculties.keys()))
    department = random.choice(faculties[faculty])
    childhood_dream_course = random.choice(dream_courses)
    current_course = department if random.random() > 0.3 else random.choice(dream_courses) 
     # 70% chance they are not studying dream course
    studying_dream_course = "Yes" if current_course == childhood_dream_course else "No"
    reason_not_studying = random.choice(reasons) if studying_dream_course == "No" else "N/A"
    would_study_dream = random.choice(["Yes", "No"])
    satisfaction = random.choice(satisfaction_levels)
    
    students.append([full_name, gender, age, faculty, department, childhood_dream_course, current_course, studying_dream_course, reason_not_studying, would_study_dream, satisfaction])

# Convert to DataFrame
df = pd.DataFrame(students, columns=[
    "Full Name", "Gender", "Age", "Faculty", "Department", "Childhood Dream Course", 
    "Current Course", "Studying Dream Course", "Reason Not Studying", "Would Study Dream", "Satisfaction"
])
print(df)
# Save dataset to CSV
df.to_csv("students_data.csv", index=False)
#print("Synthetic dataset created and saved as 'students_data.csv'")




#. Load and Analyze the Data

# Load dataset
df = pd.read_csv("students_data.csv")

# Summary statistics
print(df.describe())

# Count of students studying their childhood dream course
print(df["Studying Dream Course"].value_counts())

# Most common childhood dream courses
print(df["Childhood Dream Course"].value_counts().head(5))

# Most common reasons for not studying dream course
print(df["Reason Not Studying"].value_counts())

# Satisfaction distribution
print(df["Satisfaction"].value_counts())


#3. Visualizing the Data

import seaborn as sns
import matplotlib.pyplot as plt

# Countplot of students studying their dream course
sns.countplot(x=df["Studying Dream Course"])
plt.title("Students Studying Their Childhood Dream Course")
plt.show()

# Most common childhood dream courses
sns.countplot(y=df["Childhood Dream Course"], order=df["Childhood Dream Course"].value_counts().index)
plt.title("Most Common Childhood Dream Courses")
plt.show()

# Reasons for not studying dream course
sns.countplot(y=df["Reason Not Studying"], order=df["Reason Not Studying"].value_counts().index)
plt.title("Reasons for Not Studying Dream Course")
plt.show()

# Satisfaction levels
sns.countplot(x=df["Satisfaction"], order=["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"])
plt.title("Satisfaction Levels Among Students")
plt.show()
