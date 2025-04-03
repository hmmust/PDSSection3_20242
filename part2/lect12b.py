import numpy as np
arr1 = np.array([10,20,10,20,15,13,17,9])
arr1_filter1 =[True, True,True,False,True,False, True,False]
arr2 = arr1[arr1_filter1]
print(arr2)
arr1_filter2 = arr1 > 15 
print(arr1[arr1_filter2])