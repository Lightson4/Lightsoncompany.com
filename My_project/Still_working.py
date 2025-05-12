
import numpy as np
import pandas as pd
from Section_A import get_section_A
from Section_B import get_section_B
from Section_C import get_section_C

# Step 1: Collect data from the three sections
section_a = get_section_A()
section_b = get_section_B()
section_c = get_section_C()

# Step 2: Combine all sections into a single dictionary
if len(section_a["Fullname"]) == len(section_b["Dream course"]) == len(section_c["Satisfied_level"]):
    combined_data = {**section_a, **section_b, **section_c}

    # Step 3: Convert to DataFrame
    df = pd.DataFrame(combined_data)

    # Step 4: Save to CSV with serial numbers
    df.index += 1
    df.to_csv("student_info.csv", index_label='S/N')

    print("DataFrame created and saved as 'student_info.csv':\n")
    print(df.head())  # Print just the top rows for a preview

else:
    print("Mismatch in data lengths!")
    print(f"Section A: {len(section_a['Fullname'])} entries")
    print(f"Section B: {len(section_b['Dream course'])} entries")
    print(f"Section C: {len(section_c['Satisfied_level'])} entries")

# ================== Step 5: Data Visualization ==================

import matplotlib.pyplot as plt
import seaborn as sns

# Set theme
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Helper function to plot countplots
def plot_count(data, column, title, xlabel_rotation=45):
    sns.countplot(data=data, x=column, order=data[column].value_counts().index, palette="Set2")
    plt.title(title, fontsize=16)
    plt.xticks(rotation=xlabel_rotation)
    plt.tight_layout()
    plt.show()

# Fullname
plot_count(df, "Fullname", "Fullname Distribution")

# Gender
plot_count(df, "Gender", "Gender Distribution")

# Age
plot_count(df, "Age", "Age Distribution")

# Faculty
plot_count(df, "Faculty", "Faculty Distribution")

# Department
plot_count(df, "Dept", "Department Distribution")

# Dream Course
plot_count(df, "Dream course", "Childhood Dream Course Distribution")

# Current Course
plot_count(df, "Current course", "Current Course of Study Distribution")

# Studying Childhood Course
plot_count(df, "Studing your childhood course", "Are You Studying Your Childhood Dream Course?")

# Reasons for Not Studying Childhood Course
plot_count(df, "Reasons of Not", "Reasons for Not Studying Childhood Dream Course", xlabel_rotation=90)

# Can You Still Study It?
plot_count(df, "Can you still study it?", "Can You Still Study Your Dream Course?")

# Why Studying Current Course?
plot_count(df, "why studying current course?", "Reasons for Studying Current Course", xlabel_rotation=90)

# Satisfaction Level
plot_count(df, "Satisfied_level", "Satisfaction with Current Course")

# Practice in Real Life
plot_count(df, "Practice in real life?", "Will You Practice This Course in Real Life?")




# Histogram for Age distribution
plt.figure(figsize=(12, 6))
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # convert to numeric, ignore invalids
sns.histplot(data=df, x='Age', bins=10, kde=True, color="skyblue")
plt.title("Age Distribution", fontsize=16)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a crosstab of Faculty vs Dream Course
dream_course_count = pd.crosstab(df['Faculty'], df['Dream course'])

# Optional: Filter to top N dream courses to avoid overcrowding
top_dreams = df['Dream course'].value_counts().nlargest(5).index  # Top 5
filtered_dreams = dream_course_count[top_dreams]

# Plot the grouped bar chart
filtered_dreams.plot(kind='bar', figsize=(14, 7), colormap='Set2')
plt.title("Top Dream Courses by Faculty", fontsize=16)
plt.xlabel("Faculty")
plt.ylabel("Number of Students")
plt.xticks(rotation=45, ha='right')
plt.legend(title="Dream Course")
plt.tight_layout()
plt.show()
