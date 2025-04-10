import pandas as pd
import numpy as np
q1 = pd.Series(50,index=['mira','khalid','lana'])
print(q1)
print(q1['mira'])
print(q1[['mira','khalid']])
print(q1.ndim,q1.size,q1.empty,q1.dtype)
print(q1.head(2),q1.tail(2))



