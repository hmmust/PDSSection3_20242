import pandas as pd
import numpy as np
df1 = pd.read_csv('./part3/students.csv')
print(df1)
print(df1.ndim,df1.size,df1.empty)
print(df1.dtypes)
print(df1.head(2),df1.tail(2))
print(df1.info())
print(df1.describe())
print(df1.describe(include=['object']))



