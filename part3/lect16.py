import pandas as pd
import numpy as np
df1 = pd.DataFrame({'first':np.array([22,25,20],dtype=np.int32),
                    'second':np.array([25,21,25],dtype=np.int32),
                    'major':np.array(['DSAI','CS','SE'],dtype=str)},
                   index=['mira','khalid','lana'])
print(df1)
df1 = pd.DataFrame({'first':pd.Series([22,25,20],dtype=np.int32,
                                      index=['mira','lana','khalid']),
                    'second':pd.Series([25,21,25],dtype=np.int32,
                                       index=['mira','khalid','lana']),
                    'major':pd.Series(['DSAI','CS'],dtype=str,
                                      index=['mira','khalid'])})
print(df1)
"""print(q1.ndim,q1.size,q1.empty,q1.dtype)
print(q1.head(2),q1.tail(2))"""



