import visualization


plt.figure(figsize=(10, 6))
df["Satisfied_level"].value_counts().plot(kind="bar")
plt.title("Satisfied_level Distribution")
plt.xlabel("Satisfied_level")
plt.ylabel("Count")
plt.show()
