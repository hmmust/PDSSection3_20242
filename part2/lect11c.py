import numpy as np
arr1 = np.array([10,20,10,20,15,13,17,9])
arr2 = np.array([10,20,40,50])
print(arr2[[True, True, False,False]])
f1 = [True, False, False,False]
print(arr2[f1])
f2 = arr1 %2==0
print(arr1[f2])
f3 = arr1>=15
print(arr1[f3],f3)