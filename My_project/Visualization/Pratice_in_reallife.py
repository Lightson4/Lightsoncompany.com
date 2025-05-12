import visualization


plt.figure(figsize=(10, 6))
df["Practice in real life?"].value_counts().plot(kind="bar")
plt.title("Practice in Real Life Distribution")
plt.xlabel("Practice in Real Life")
plt.ylabel("Count")
plt.show()
