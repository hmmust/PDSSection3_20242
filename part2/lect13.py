import numpy as np #slicing, indexing 
arr1 = np.array([10,20,10,20,15,13,17,9])
arr3 = np.array([[13,17,7,15],[12,3,22,19]])
print(arr1[3]) #indexing
print(arr1[0:4]) #slicing
print(arr1[0:4:2]) #slicing
print(arr1[-1]) 
print(arr1[7]) 
print(arr1[len(arr1)-1]) 
print(arr1[-2:]) 
print(arr1[::-1]) 
print(arr3[1,0]) #indexing
print(arr3[1,0:5]) #indexing
print(arr3[1,:]) #indexing
print(arr3[1,0:]) #indexing
print(arr3[1,...]) #indexing