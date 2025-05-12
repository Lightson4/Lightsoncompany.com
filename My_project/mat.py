import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Create a simple scatter plot
'''
x = [1,2,3,4,5,]
y = [1,4,9,16,25]
#Create a line plot
plt.plot(x,y, marker = "*", linestyle= "--", color= "g")
plt.xlabel("x axis")
plt.ylabel("Y Axis")
plt.title("Graphic Line Plot")
plt.grid(True)
plt.show()

#Multiples plots
#Sample data
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.figure(figsize=(9,5))

plt.subplot(2,2,1)
plt.plot(x,y1,color='green')
plt.title("Plot 1")

plt.subplot(2,2,2)
plt.plot(y1,x,color='red')
plt.title("Plot 2")
plt.grid(True)

plt.subplot(2,2,3)
plt.plot(x,y2,color='blue')
plt.title("Plot 3")

plt.subplot(2,2,4)
plt.plot(x,y2,color='green')
plt.title("Plot 4")
plt.grid(True)
plt.show()

x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x,y,color= "pink", marker="o")
plt.title("Scatter Plot")
plt.xlabel("x Values")
plt.ylabel("Y Values")
plt.show()

#Bar Plot
categories =["A",'B','C','D','E']
values= [5,7,3,8,9]
#Create a bar plot
plt.bar(categories,values, color="black")
plt.xlabel("categories")
plt.ylabel("values")
plt.title("Bar Chart")
plt.show()
'''

#Histogram
#  Sample Data
data = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
#create a historgram 
plt.hist(data,bins=5, color="red", edgecolor="green")
plt.show()

#scatter plot
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.scatter(x,y,color="black", marker="*")
plt.title("scatrer Plot")
plt.show()
'''
#pie Chart
labels=["A","B","C","D"]
sizes= [30,20,50,67]
colors=["Gold", "yellow","skyblue","brown"]
explode=[0,0,0.2,0] #move out the third slice
#create a Pie Chart
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct="%1.1f%%",shadow=True)
plt.show()
'''
#pygrame