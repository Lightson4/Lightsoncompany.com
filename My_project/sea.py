import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Generate a 5x5 matrix with random values
data = np.random.rand(5,5)
#create a heatmap
sns.heatmap(data, annot=True,cmap="coolwarm")
plt.title("Seaborn Heatmap example")
plt.show()


# Generate sample data
np.random.seed(10)
x = np.linspace(1, 10, 50)
y = np.sin(x) + np.random.normal(0, 0.2, size=50)
data = pd.DataFrame({"X": x, "Y": y})

# Create line plot
sns.lineplot(x="X", y="Y", data=data, ci="sd")
plt.title("Seaborn Line Plot with Confidence Interval")
plt.show()