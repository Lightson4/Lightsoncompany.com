import visualization

plt.figure(figsize=(10, 6))
df["Current course"].value_counts().plot(kind="bar")
plt.title("Current Course Distribution")
plt.xlabel("Current Course")
plt.ylabel("Count")
plt.show()
