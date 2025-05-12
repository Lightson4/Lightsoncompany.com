import visualization

plt.figure(figsize=(10, 6))
df["Can you still study it?"].value_counts().plot(kind="bar")
plt.title("Can you still study it Distribution")
plt.xlabel("Can you still study it")
plt.ylabel("Count")
plt.show()