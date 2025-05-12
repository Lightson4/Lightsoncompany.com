import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import Section_A as section_a
import Section_B as section_b
import Section_C as section_c

# Step 1: Manually define the mock data for each section with 60 students
student_data = []
for i in range(1, 61):  # Loop through to create data for 60 students
    section_a = {
        'Full Name': f'Student {i}',
        'Gender': 'Male' if i % 2 == 0 else 'Female',  # Alternating genders
        'Age': '18-25' if i % 2 == 0 else '26-35',  # Alternating age groups
        'Faculty': 'Engineering',
        'Dept': 'Computer Science'
    }

    section_b = {
        'Dream course': 'Software Engineering' if i % 2 == 0 else 'Data Science',
        'Studing your childhood course': 'Yes' if i % 2 == 0 else 'No'
    }

    section_c = {
        'Current course': 'Computer Science',
        'Reasons of Not': 'N/A',
        'Can you still study it?': 'Yes',
        'why studying current course?': 'Interest in technology',
        'Satisfied_level': 'Very Satisfied',
        'Practice in real life?': 'Yes'
    }

    # Combine all sections into one record
    student_record = {**section_a, **section_b, **section_c}
    student_data.append(student_record)

# Step 2: Convert to DataFrame
df = pd.DataFrame(student_data)

# Save to CSV
df.to_csv("student_info.csv", index_label="S/N")

# Check for missing values and duplicates
print("Missing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# Step 3: Plot the distributions (bar charts)
plt.figure(figsize=(10, 6))
sns.countplot(x="Gender", data=df)
plt.title("Gender Distribution")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x="Age", data=df)
plt.title("Age Distribution")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x="Dream course", data=df)
plt.title("Dream Course Distribution")
plt.show()
