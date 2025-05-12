#1
import numpy as np
import pandas as pd

arr = pd.DataFrame(np.random.randint(1, 100,size=(5, 5)), columns=["q", "w", "e", "r", "t"], index=["a", "s", "d", "f", "g"])
value= arr **2
print(f"value:", value)
print("original array:,")
print(arr)
'''#replacing the thrid column with 1
arr[:, 3] = 1
print("\nModified array:")
print(arr)
#2 question another example
arr1 = np.random.randint(1, 17, size=(4,4))
print(f"arr1:", arr1)
arr1[:, 3] = 0
print("\n2modidfy:")
print(arr1)
#3 question
arr2 = np.arange(1, 37).reshape(6, 6)
print("original array:",)
print(arr2) #extrat the sub-array consisting of the 3rd to 5th rows and columns 
sub_arr = arr2[3:5, 2:4]
print("\nsub_arr:")
print(sub_arr)
#4 question
arr3 = np.random.randint(1, 100, size=(4, 4))
print("arr3:",)
print(arr3)
#5
arr4 = np.array.reshape(3+5)
arr4 = np.array([3 - 5,])
arr4 = np.array([3 / 5,])
arr4 = np.array([3 * 5,])
arr4.reshape
print(f"arr4:", arr4)
#6
arr5 = np.array(1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20)
arr5.reshape([4,4])
print(arr5)
#7
arr5 = np.array(1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20)
arr5.reshape([5,5])
mean = np.mean(arr5)
std_dev = np.std(arr5)
median = np.median(arr5)
print(arr5)
'''