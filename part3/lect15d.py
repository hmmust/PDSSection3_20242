import pandas as pd
import numpy as np
df1 = pd.DataFrame([10,20,30],columns=['mark']
    ,index=['mira','khalid','lana'])
print(df1)
df3 = pd.DataFrame([[22,25,'DSAI'],[25,21,'CS'],
                    [20,25,'SE']],
                   columns=['first','second','major'],
                   index=['mira','khalid','lana'])
print(df3)
df4 = pd.DataFrame({'first':[22,25,20],
                    'second':[25,21,25],
                    'major':['DSAI','CS','SE']},
                   index=['mira','khalid','lana'])
print(df4)
print(df4.major.count())
"""print(q1.ndim,q1.size,q1.empty,q1.dtype)
print(q1.head(2),q1.tail(2))"""



