import numpy as np
#creating arrays using numpy
arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
print(arr1.shape)
arr2 = np.array ([1,2,3,4,5,6,7])
arr2.reshape(1,7)
print(arr2)
#2 dementional array
arr3 = np.array([[1,2,3,4,5,], [2,3,4,5,6]])
print(f"arr3:", arr3)
print(arr3.shape)
# another exam
arr4 = np.array([[4,3,2], [2,9,5]])
print(arr4)
print(arr4.shape)
ar = np.arange(0, 10, 2).reshape(5,1)
print(ar)
ar2 = np.arange(0, 12, 3).reshape(2,2)
print(ar2)

#3dimentional arrays
ar4 = np.array([[1,3,5], [6, 9, 2], [7, 3, 8]])
print(ar4.shape)
print(ar4)
Academe = np.array([["digital mgk", 'Data ana', 'software eng', 'web design', 'cyber', 'painting'], ["victor", 'light','solomon', 'prince', 'blessing', 'ben']])
print(f"Academe:", Academe)
#other functions like ones, zeros,eye, etc
ar5 = np.ones((6,7))
print(ar5)
ar6 = np.eye(4)
print(ar6)
arr7 = np.array(([3,5], [6,3]))
print(f"arr7:", arr7)
print(arr7.shape)
print(arr7.ndim)
print(arr7.size)
print(arr7.dtype)
print(arr7.itemsize)
#numpy vectorize opperation
arr8 = np.array([1,2,3,4,5,6,7,8,9])
arr9 = np.array([21, 32,45,6,75,3,35,5,8,])
print(arr8 + arr9)
print(arr8 - arr9)
print(arr8 * arr9)
print(arr8 / arr9)
#universal function
light = np.array([1,2,3,44,5,6,7,8,9])
print(np.sqrt(light))
#expotential
print(np.exp(light))
#sine
print(np.sin(light))
#log
print(np.log(light))
#slizing and indencing
light2 = np.array(([1,2,3,4],[6,3,2,3], [5,7,8,6]))
print("Array : \n", light2)
print(light2[1:,1:3])
print(light2[0][0])
#calcalting mean and standared deviation
data = ([1,2,3,4,5,6])
mean = np.mean(data)
std_dev = np.std(data)
normalize_data = (data - mean) / std_dev
print("normalize_data:", normalize_data)
print("std:", std_dev)
print(mean)
# for median
median = np.median(data)
print("median:", median)
#veriance
variance = np.var([1,2,3,4,5,6])
print('variance:', variance)
#[for mode no mode]
Mod = np.mod(data)
print('mod:', Mod)
#logical operation
info = np.array([1,2,3,4,5,6,7,8,9,10])
tuple_list = info[(info >= 5) & (info <= 8)]
print(tuple_list)
#more
info2 =np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
tuple_list2 = info2[(info2 >= 10) & (info2 <= 20)]
print(tuple_list2)
print(tuple_list2.shape)
#common operation
arr =np.array ([1,2,3,4,5,6,7,8,9])
arr1 =np.array([1,2,3,3,4,6,7,2,8,])
common_element = np.intersect1d(arr, arr1)
print("common_element:", common_element)
addition_elements = np.add(arr, arr1)
print("addition_elements:", addition_elements)
#multpy element
multipy_element = np.multiply(arr , arr1)
print('multipy_element:', multipy_element)
#substract
substract =np.subtract(arr, arr1)
print("substract:", substract)
#sum_element
sum_element =np.sum([arr, arr1])
print(sum_element)
print("sum_element:", sum_element)
#universail function
universal_element =np.union1d(arr, arr1)
print("universal:", universal_element)
arr2 =np.array([1,2,3,4,5])
diffence_element = np.setdiff1d(arr1, arr2)
print("diffence_element:", diffence_element)
arr3 =np.array([4,5,6,7])
symmetric_differnce = np.setxor1d(arr1 , arr3)
print("symmetric:", symmetric_differnce)

import numpy as np 
Oluchi = np.array([1,2,3,4,5,6,7,8,9])
mean = np.mean(Oluchi)
print("Oluchi:", mean)
