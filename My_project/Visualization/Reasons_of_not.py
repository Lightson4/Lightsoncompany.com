import visualization


plt.figure(figsize=(10, 6))
df["Reasons of Not"].value_counts().plot(kind="bar")
plt.title("Reasons of Not Distribution")
plt.xlabel("Reasons of Not")
plt.ylabel("Count")
plt.show()
