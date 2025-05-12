import visualization


plt.figure(figsize=(10, 6))
df["Faculty"].value_counts().plot(kind="bar")
plt.title("Faculty Distribution")
plt.xlabel("Faculty")
plt.ylabel("Count")
plt.show()