import pandas as pd
import numpy as np
df1 = pd.read_csv('./part3/students.csv')
print(df1[ (df1['Age']>20) &  (df1['Major']=='DS')])




