import pandas as pd
import numpy as np
q1 = pd.Series(np.arange(1,20))
q2 = pd.Series(np.random.randint(10,20,size=10))
q3 = pd.Series([i*10 for i in range(10,20)])
print(q1)
print(q2)
print(q3)


"""print(q1['mira'])
#print(q1[0]) #error
print(q1[0:2])
print(q1[-1:])
q2 = pd.Series({'mira':1,'khalid':2,'lana':2})
print(q2)"""