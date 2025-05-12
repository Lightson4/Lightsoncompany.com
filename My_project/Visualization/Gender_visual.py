import visualization
# Plot a bar chart for the count of each unique value
plt.figure(figsize=(10, 6))
df["Gender"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
