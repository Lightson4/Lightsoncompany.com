'''num = float(input())
if num > 0:
 print(num, "is positive number")
elif num < 0:
 print(num, "is negetive number")
else:
 print(num, "is zero")

 def factorial(n):
 if n == 0:
  return 1
 else:
  return n * factorial(n-1)
num = int(input("Enter a number: "))
print(f" the factorial id {num} is {factorial(num)}")

numbers = [45, 65, 78, 98, 23, 74, 85, 90]
print(f"original list", numbers)
print(f"sorted list:", numbers.sort)
'''
import pandas as pd
import numpy as np
arre = pd.DataFrame(np.random.randint(1, 100, size=(3,5)))
double = arre **2
double = lambda x:x *2
print(double(10))