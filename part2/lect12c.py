import numpy as np
arr1 = np.array([10,20,10,20,15,13,17,9])
print(arr1.shape,arr1.ndim)
arr2 = np.array([[10,20,10,20,3],[15,13,17,9,4]])
print(arr2.shape,arr2.ndim)
arr3 = arr1.reshape((4,2))
print(arr3)
arr4 = arr2.reshape((5,2))
print(arr4)
print(arr4.reshape(-1))