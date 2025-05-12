import visualization

plt.figure(figsize=(10, 6))
df["Dept"].value_counts().plot(kind="bar")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()
