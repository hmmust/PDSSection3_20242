import pandas as pd
q1 = pd.Series([1,2,2,3], # np.array([[1,2,2,3]])
               index=['mira','khalid','lana','moh'])
print(q1)
print(q1['mira'])
#print(q1[0]) #error
print(q1[0:2])
print(q1[-1:])
q2 = pd.Series({'mira':1,'khalid':2,'lana':2})
print(q2)