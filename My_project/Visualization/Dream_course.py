import visualization


plt.figure(figsize=(10, 6))
df["Dream course"].value_counts().plot(kind="bar")
plt.title("Dream course Distribution")
plt.xlabel("Dream Course")
plt.ylabel("Count")
plt.show()