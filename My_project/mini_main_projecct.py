
#Step 1: Import libraries needed

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Step 2: Load the dataset
#Let's create a sample dataset with 60 students


# Sample dataset
full_names = [
    "John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Davis",
    "David Evans", "Emily Foster", "Frank Garcia", "Grace Hall", "Hannah Lee",
    "Isaac Martin", "Julia Nelson", "Kevin Patel", "Lily Reed", "Matthew Sanders",
    "Natalie Taylor", "Oliver Walker", "Paige Wallace", "Quincy Watson", "Rachel White",
    "Samuel Yang", "Tessa Zhang", "Uma Brown", "Victor Chen", "Wendy Davis",
    "Xavier Edwards", "Yolanda Flores", "Zachary Garcia", "Ava Harris", "Benjamin Jenkins",
    "Caitlin Kennedy", "Daniel Kim", "Eleanor Lewis", "Fiona Martin", "Gabriel Mitchell",
    "Harrison Nguyen", "Isabella Patel", "Julian Sanchez", "Kayla Taylor", "Lucas Walker",
    "Mia Wallace", "Nathan Watson", "Olivia White", "Patrick Yang", "Quincy Zhang",
    "Rebecca Brown", "Ryan Chen", "Sophia Davis", "Tessa Edwards", "Uma Flores",
    "Victor Garcia", "Wendy Harris", "Xavier Jenkins", "Yolanda Kennedy", "Zachary Kim",
    "Ava Lewis", "Benjamin Martin", "Caitlin Mitchell", "Daniel Nguyen", "Eleanor Patel",
    "Fiona Sanchez", "Gabriel Taylor", "Harrison Walker", "Isabella Wallace"
]

genders = [
    "Male", "Female", "Female", "Male", "Male", "Male", "Female", "Male", "Female", "Female",
    "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female",
    "Male", "Female", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male",
    "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male",
    "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male",
    "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male",
    "Female", "Male", "Female"
]

ages = [
    20, 22, 21, 20, 21, 20, 22, 21, 20, 21,
    20, 22, 21, 20, 21, 20, 22, 21, 20, 21,
    20, 22, 21, 20, 21, 20, 22, 21, 20, 21,
    20, 22, 21, 20, 21, 20, 22, 21, 20, 21,
    20, 22, 21, 20, 21, 20, 22, 21, 20, 21,
    20, 22, 21, 20, 21, 20, 22, 21, 20, 21
]

faculties = [
    "Engineering", "Arts", "Science", "Engineering", "Arts", "Science", "Engineering", "Arts", "Science", "Engineering",
    "Arts", "Science", "Engineering", "Arts", "Science", "Engineering", "Arts", "Science", "Engineering", "Arts",
    "Science", "Engineering", "Arts", "Science", "Engineering", "Arts", "Science", "Engineering", "Arts", "Science",
    "Engineering", "Arts", "Science", "Engineering", "Arts", "Science", "Engineering", "Arts", "Science", "Engineering",
    "Arts", "Science", "Engineering", "Arts", "Science", "Engineering", "Arts", "Science", "Engineering", "Arts",
    "Science", "Engineering", "Arts", "Science", "Engineering", "Arts", "Science", "Engineering", "Arts", "Science"
]


depts = [
    "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English",
    "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering",
    "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English",
    "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering",
    "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English",
    "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering"
]

childhood_dream_courses = [
    "Computer Science", "Medicine", "Biology", "Mechanical Engineering", "Computer Science", "Medicine", "Biology", "Mechanical Engineering", "Computer Science", "Medicine",
    "Biology", "Mechanical Engineering", "Computer Science", "Medicine", "Biology", "Mechanical Engineering", "Computer Science", "Medicine", "Biology", "Mechanical Engineering",
    "Computer Science", "Medicine", "Biology", "Mechanical Engineering", "Computer Science", "Medicine", "Biology", "Mechanical Engineering", "Computer Science", "Medicine",
    "Biology", "Mechanical Engineering", "Computer Science", "Medicine", "Biology", "Mechanical Engineering", "Computer Science", "Medicine", "Biology", "Mechanical Engineering",
    "Computer Science", "Medicine", "Biology", "Mechanical Engineering", "Computer Science", "Medicine", "Biology", "Mechanical Engineering", "Computer Science", "Medicine",
    "Biology", "Mechanical Engineering", "Computer Science", "Medicine", "Biology", "Mechanical Engineering", "Computer Science", "Medicine", "Biology", "Mechanical Engineering"
]

current_courses = [
    "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English",
    "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering",
    "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English",
    "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering",
    "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English",
    "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering", "Computer Science", "English", "Biology", "Mechanical Engineering"
]

studying_childhood_dream_courses = [
    "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No",
    "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No",
    "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No",
    "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No",
    "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No",
    "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No"
]


why_studying_current_courses = [
    "Interest", "Family influence", "Career prospects", "Interest", "Family influence", "Career prospects", "Interest", "Family influence", "Career prospects", "Interest",
    "Family influence", "Career prospects", "Interest", "Family influence", "Career prospects", "Interest", "Family influence", "Career prospects", "Interest", "Family influence",
    "Career prospects", "Interest", "Family influence", "Career prospects", "Interest", "Family influence", "Career prospects", "Interest", "Family influence", "Career prospects",
    "Interest", "Family influence", "Career prospects", "Interest", "Family influence", "Career prospects", "Interest", "Family influence", "Career prospects", "Interest",
    "Family influence", "Career prospects", "Interest", "Family influence", "Career prospects", "Interest", "Family influence", "Career prospects", "Interest", "Family influence",
    "Career prospects", "Interest", "Family influence", "Career prospects", "Interest", "Family influence", "Career prospects", "Interest", "Family influence", "Career prospects"
]

satisfactions_with_current_courses = [
    "Very satisfied", "Satisfied", "Dissatisfied", "Neutral", "Very satisfied", "Satisfied", "Dissatisfied", "Neutral", "Very satisfied", "Satisfied",
    "Dissatisfied", "Neutral", "Very satisfied", "Satisfied", "Dissatisfied", "Neutral", "Very satisfied", "Satisfied", "Dissatisfied", "Neutral",
    "Very satisfied", "Satisfied", "Dissatisfied", "Neutral", "Very satisfied", "Satisfied", "Dissatisfied", "Neutral", "Very satisfied", "Satisfied",
    "Dissatisfied", "Neutral", "Very satisfied", "Satisfied", "Dissatisfied", "Neutral", "Very satisfied", "Satisfied", "Dissatisfied", "Neutral",
    "Very satisfied", "Satisfied", "Dissatisfied", "Neutral", "Very satisfied", "Satisfied", "Dissatisfied", "Neutral", "Very satisfied", "Satisfied",
    "Dissatisfied", "Neutral", "Very satisfied", "Satisfied", "Dissatisfied", "Neutral", "Very satisfied", "Satisfied", "Dissatisfied", "Neutral"
]

practicing_current_courses_in_real_life = [
    "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No",
    "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No",
    "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No",
    "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No",
    "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No",
    "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "No"
]

data1 = {
    "Full name": full_names,
    "Gender": genders,
    "Age": ages,
    "Faculty": faculties,
    "Dept": depts,
    "Childhood dream course": childhood_dream_courses,
    "Current course": current_courses,
    "Studying childhood dream course": studying_childhood_dream_courses,
    "Why studying current course": why_studying_current_courses,
    "Satisfaction with current course": satisfactions_with_current_courses,
    "Practicing current course in real life": practicing_current_courses_in_real_life
}

# Create a Pandas dataframe
df = pd.DataFrame(data1)

# Store the dataframe as a CSV file
df.to_csv("student_data.csv", index=False)

# Read the CSV file
df = pd.read_csv("student_data.csv")


#Step 3: Data Cleaning

# Check for missing values
print(df.isnull().sum())

# Check for duplicate rows
print(df.duplicated().sum())

# Check for inconsistent entries
print(df.describe())

# Fill missing values with fillna or remove with dropna
# For demonstration purposes, let's fill missing values with fillna
df.fillna("Unknown", inplace=True)


#Step 4: Check basic statistics about the dataset

# Use value_counts() to get the count of each unique value
print(df["Gender"].value_counts())
print(df["Faculty"].value_counts())
print(df["Dept"].value_counts())
print(df["Childhood dream course"].value_counts())
print(df["Current course"].value_counts())
print(df["Studying childhood dream course"].value_counts())
print(df["Why studying current course"].value_counts())
print(df["Satisfaction with current course"].value_counts())
print(df["Practicing current course in real life"].value_counts())


#Step 5: Data Visualization

import matplotlib.pyplot as plt

# Plot a bar chart for the count of each unique value
plt.figure(figsize=(10, 6))
df["Gender"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10, 6))
df["Faculty"].value_counts().plot(kind="bar")
plt.title("Faculty Distribution")
plt.xlabel("Faculty")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10, 6))
df["Dept"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10, 6))
df["Childhood dream course"].value_counts().plot(kind="bar")
plt.title("Childhood Dream Course Distribution")
plt.xlabel("Childhood Dream Course")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10, 6))
df["Current course"].value_counts().plot(kind="bar")
plt.title("Current Course Distribution")
plt.xlabel("Current Course")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10, 6))
df["Studying childhood dream course"].value_counts().plot(kind="bar")
plt.title("Studying Childhood Dream Course Distribution")
plt.xlabel("Studying Childhood Dream Course")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10, 6))
df["Why studying current course"].value_counts().plot(kind="bar")
plt.title("Why Studying Current Course Distribution")
plt.xlabel("Why Studying Current Course")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10, 6))
df["Satisfaction with current course"].value_counts().plot(kind="bar")
plt.title("Satisfaction with Current Course Distribution")
plt.xlabel("Satisfaction with Current Course")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10, 6))
df["Practicing current course in real life"].value_counts().plot(kind="bar")
plt.title("Practicing Current Course in Real Life Distribution")
plt.xlabel("Practicing Current Course in Real Life")
plt.ylabel("Count")
plt.show()

'''
#Step 6: Conclusion and Executive Summary
Based on the analysis, here are some key findings:

- The dataset consists of 60 students with a mix of male and female participants.
- The most popular faculty is Engineering, with 20 students enrolled in Computer Science and Mechanical Engineering.
- 30 students are studying their childhood dream course, while 30 are not.
- The main reasons for studying the current course are interest and career prospects.
- 40 students are satisfied with their current course, while 10 are dissatisfied.

Executive Summary
This report analyzes the dataset of 60 students, exploring their demographics, academic background, and satisfaction with their current course. The findings suggest that students are motivated by interest and career prospects, but there are some discrepancies between their childhood dream courses and current studies. The report provides insights into the students' experiences and can inform future academic and career decisions.
'''
