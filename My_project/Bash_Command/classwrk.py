import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#class work on Matplotlib
RD = pd.read_csv("data.csv")
#print(RD)
rd=pd.DataFrame("RD")
Sales=np.random.rand(1000, 10000)
Value=np.random.rand(1000, 10000)
plt.xlabel("Sales")
plt.ylabel("Value")
plt.title("CSV")
plt.show()

