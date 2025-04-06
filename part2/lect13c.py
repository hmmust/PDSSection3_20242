import numpy as np
arr1 = np.array([10,20,10,20,15,13,17,9])
s1 = np.where(arr1>10)
print(s1)
print(arr1[[0,1]])
print(arr1[[1,0,1]])
print(arr1[s1])


