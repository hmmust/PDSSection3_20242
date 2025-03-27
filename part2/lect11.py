import numpy as np
arr2 = np.array([10,20.5,10],dtype=np.float32) #'f' float
arr2= np.sort(arr2)
print(arr2,type(arr2),arr2.dtype)
arr3 = np.array([[10,20,30],[40,50,0]],dtype=np.int16)
print(arr3,type(arr3),arr3.dtype)
arr4 = arr3.astype(np.bool)
print(arr4)
