import visualization


plt.figure(figsize=(10, 6))
df["why studying current course?"].value_counts().plot(kind="bar")
plt.title("why Studying Current Course Distribution")
plt.xlabel("why Studying Current Course")
plt.ylabel("Count")
plt.show()