import numpy as np
arr2 = np.array([10,20,10,20,15,13,17,9])
arr3 = np.array([[10,20,30],[40,50,0]])
arr2_r = arr2.reshape(4,2)
arr2_r2 = arr2.reshape(2,4)
arr3_r = arr3.reshape(3,2)
print(arr2_r,arr2_r2)
print(arr3_r)
#flattening
arr3_flatten= arr3.reshape(-1)
print(arr3_flatten)
