#example of function
def sum_even_numbers():
    print([1,2,3,4,5,6])
sum_even_numbers()

#pandas eg.
import pandas as pd
import numpy as np
data= pd.DataFrame(np.random.randint(1, 100, size=(5,3)), columns=['A','B','C'])
print(data)
#data clearing eg
data = {
    'A': [10, np.nan, 30], 
    'B': [np.nan, 50, 60]
    }
df = pd.DataFrame(data)
#print(df.mean)
# Your code here to fill missing values
df.fillna('Unknown', inplace=True)
print(df.mean)
'''
def Greet ():
    print("hello, welcome to AWT academy")
Greet()
'''
#matplotlib eg
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[0.1,0.2,0.3,0.4,0.5,0.6]
#plt.xlabel('x axis')
#plt.ylabel('y axis')
plt.scatter(x,y, color='blue',marker='*')
plt.title("simple plot example")
plt.show()


#eg of set
unique_set= {1,2,3,4,5,6,7}
print(unique_set)