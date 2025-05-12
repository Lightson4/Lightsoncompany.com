import numpy as np
#no 1
arr = np.random.randint(1, 21, size=(5, 5))
print("Original Array:")
print(arr)
# replace all element in column 3
arr[:, 2] = 1
print(arr)

#No 2
#Create a Numpy of shape (4,4) with values from 1 
arr1 = np.arange(1, 17).reshape(4,4)
print(f"arr1:", arr1)
#replacing the diogonal element wwith 0
np.fill_diagonal(arr1, 0)
print(arr1)

#no 3
arr2 = np. arange(1, 37).reshape(6,6)
print("origial array")
print(arr2)
#extrating thee sub array consisting of the 3rd to 5th rows and 2nd to 4th columns
sub_arr = arr[3:5, 2:4]
print("\nSub-array:")
print(sub_arr)

#no 4
arr3 = np.random.randint(1, 100, size=(5,  5))
print("orfiginal arr3:")
print(arr3)

# Extract the elements on the border\\\\\\\\\\\
border_elements = np.concatenate((arr[0, :], arr[-1, :], arr[:, 0], arr[:, -1]))
print("\nBorder Elements:")
print(border_elements)


#no 5

# Create two NumPy arrays of shape (3, 4) filled with random integers
arr1 = np.random.randint(1, 100, size=(3, 4))
arr2 = np.random.randint(1, 100, size=(3, 4))

print("Array 1:")
print(arr1)
print("\nArray 2:")
print(arr2)

# Perform element-wise addition, subtraction, multiplication, and division
addition = arr1 + arr2
subtraction = arr1 - arr2
multiplication = arr1 * arr2
division = arr1 / arr2

print("\nElement-wise Addition:")
print(addition)
print("\nElement-wise Subtraction:")
print(subtraction)
print("\nElement-wise Multiplication:")
print(multiplication)
print("\nElement-wise Division:")
print(division)

#no 6

# Create a NumPy array of shape (4, 4) with values from 1 to 16
arr = np.arange(1, 17).reshape(4, 4)
print("Original Array:")
print(arr)

# Compute the row-wise and column-wise sum
row_sum = np.sum(arr, axis=1)
col_sum = np.sum(arr, axis=0)

print("\nRow-wise Sum:")
print(row_sum)
print("\nColumn-wise Sum:")
print(col_sum)

#no 7

# Create a NumPy array of shape (4, 4) with values from 1 to 16
arr = np.arange(1, 17).reshape(4, 4)
print("Original Array:")
print(arr)

# Compute the row-wise and column-wise sum
row_sum = np.sum(arr, axis=1)
col_sum = np.sum(arr, axis=0)

print("\nRow-wise Sum:")
print(row_sum)
print("\nColumn-wise Sum:")
print(col_sum)

#no 8

# Create a NumPy array of shape (5, 5) filled with random integers
arr = np.random.randint(1, 100, size=(5, 5))
print("Original Array:")
print(arr)

# Compute the mean, median, standard deviation, and variance of the array
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)
variance = np.var(arr)

print("\nMean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)


