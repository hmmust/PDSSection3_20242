import numpy as np
arr1 = np.array([10,20,10,20,15,13,17,9])
arr2 = np.array([13,17,7,15,12,3,22,19])
arr3 = np.array([[13,17,7,15],[12,3,22,19]])
arr4 = np.array([[12,11,17,5],[2,13,32,39]])
arr1_2 = np.concatenate((arr1,arr2))
print(arr1_2)
arr3_4 = np.concatenate((arr3,arr4),axis=0) #rows
arr3_4 = np.vstack((arr3,arr4)) #rows
print(arr3_4)
arr3_4b = np.concatenate((arr3,arr4),axis=1) #columns
arr3_4b = np.hstack((arr3,arr4)) #columns
print(arr3_4b)