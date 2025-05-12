# Step 1: Import modules and collect data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Section_A import get_section_A
from Section_B import get_section_B
from Section_C import get_section_C

# Get data from the sections
section_a = get_section_A()  # List of 60 dictionaries
section_b = get_section_B()
section_c = get_section_C()


print(f"Length of Section A: {len(section_a)}")
print(f"Length of Section B: {len(section_b)}")
print(f"Length of Section C: {len(section_c)}")

# Make sure all three sections are the same length
assert len(section_a) == len(section_b) == len(section_c), "Mismatch in data lengths!"

# Merge the corresponding records from each section into one student dictionary
merged_data = []
for i in range(len(section_a)):
    student = {**section_a[i], **section_b[i], **section_c[i]}
    merged_data.append(student)

# Step 2: Create DataFrame
df = pd.DataFrame(merged_data)

# Save to CSV with S/N
df.reset_index(inplace=True)
df.index += 1
df.rename(columns={"index": "S/N"}, inplace=True)
df.to_csv("student_info.csv", index=False)

# Step 3: Data Cleaning
print("Missing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
df.fillna("Unknown", inplace=True)

# Step 4: Summary Stats
columns_to_check = [
    "Gender", "Age", "Faculty", "Dept", "Dream course", "Current course",
    "Studing your childhood course", "Reasons of Not",
    "Can you still study it?", "why studying current course?", 
    "Satisfied_level", "Practice in real life?"
]

for col in columns_to_check:
    print(f"\n{col}:\n", df[col].value_counts())

# Step 5: Visualizations
def plot_count(column, title):
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x=column, order=df[column].value_counts().index)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

# Plot all visuals
for col in columns_to_check:
    plot_count(col, f"{col} Distribution")
