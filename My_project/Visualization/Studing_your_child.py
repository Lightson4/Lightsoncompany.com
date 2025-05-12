import visualization

plt.figure(figsize=(10, 6))
df["Studing your childhood course"].value_counts().plot(kind="bar")
plt.title("Studing your childhood course Distribution")
plt.xlabel("Studing your childhood course")
plt.ylabel("Count")
plt.show()
