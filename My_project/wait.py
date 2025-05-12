import pandas
import numpy
import matplotlib.pyplot

#Assuming student_daata is your dictionary

#To fill missing age values, you can use the following code:

student_data['section_a']['Age'].fillna('Unknown', inplace=True)
print(student_data)

#print("Data saved successfully to students_data.csv!")

# to fill missing values with specific values
student_data.fillna("Unknown", inplace=True)
print(student_data)
#. Load and Analyze the Data

# Summary statistics
print(df.describe())

# Summary statistics
print(df.describe())

# Count of students studying their childhood dream course
print(df["Studying your childhood Course"].value_counts())

# Most common childhood dream courses
print(df["Dream course"].value_counts().head(5))

# Most common reasons for not studying dream course
print(df["Reasons of Not"].value_counts())

# Satisfaction distribution
print(df["Satisfied_level"].value_counts())


1. Correlation Analysis (Pie Chart)

# Create a pie chart for the correlation analysis
plt.figure(figsize=(10, 6))
corr_matrix = df[["Satisfaction with Current Course", "Why Studying Current Course"]].corr()
corr_matrix.plot(kind="pie", autopct='%1.1f%%')
plt.title("Correlation Analysis")
plt.show()


2. Distribution Analysis (Pie Chart)

# Create a pie chart for the distribution analysis
plt.figure(figsize=(10, 6))
df["Studying Childhood Dream Course"].value_counts().plot(kind="pie", autopct='%1.1f%%')
plt.title("Distribution Analysis")
plt.show()


3. Faculty and Gender (Pie Chart)

# Create a pie chart for the faculty distribution
plt.figure(figsize=(10, 6))
df["Faculty"].value_counts().plot(kind="pie", autopct='%1.1f%%')
plt.title("Faculty Distribution")
plt.show()

# Create a pie chart for the gender distribution
plt.figure(figsize=(10, 6))
df["Gender"].value_counts().plot(kind="pie", autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.show()


4. Reasons for Not Studying (Word Cloud)

# Create a word cloud for the reasons why students are not studying their dream courses
from wordcloud import WordCloud
text = ' '.join(df["Why Not Studying Childhood Dream Course"].dropna())
wordcloud = WordCloud(width=800, height=400).generate(text)
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


5. Future Career Plan (Pie Chart)

# Create a pie chart for the future career plan
plt.figure(figsize=(10, 6))
df["Practicing Current Course in Real Life"].value_counts().plot(kind="pie", autopct='%1.1f%%')
plt.title("Future Career Plan")
plt.show()


6. Satisfied Level vs Dream Course (Heatmap)

# Create a heatmap for the satisfied level vs dream course
plt.figure(figsize=(10, 6))
sns.heatmap(pd.crosstab(df["Satisfaction with Current Course"], df["Studying Childhood Dream Course"]), annot=True, cmap="coolwarm")
plt.title("Satisfied Level vs Dream Course")
plt.show()


7. Age Distribution (Histogram)

# Create a histogram for the age distribution
plt.figure(figsize=(10, 6))
df["Age"].plot(kind="hist", bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()


8. Gender vs Satisfied Level (Group Bar Chart)

# Create a group bar chart for the gender vs satisfied level
plt.figure(figsize=(10, 6))
sns.countplot(x="Gender", hue="Satisfaction with Current Course", data=df)
plt.title("Gender vs Satisfied Level")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()


9. Faculty vs Dream Course (Bar Chart)

# Create a bar chart for the faculty vs dream course
plt.figure(figsize=(10, 6))
sns.countplot(x="Faculty", hue="Studying Childhood Dream Course", data=df)
plt.title("Faculty vs Dream Course")
plt.xlabel("Faculty")
plt.ylabel("Count")
plt.show()

