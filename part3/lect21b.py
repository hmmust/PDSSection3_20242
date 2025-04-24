import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')
student_ma= student_df.groupby(by=['Major','Age'])
for v in student_ma:
    print(v)
print(student_ma['Id'].count())
# average for GPAs for each Major
print(student_df.groupby(by=['Major'])['GPA'].mean())
# average for GPAs for each Major and year
print(student_df.groupby(by=['Major','Year'])['GPA'].mean())
# highest GPA for each Major and year
print(student_df.groupby(by=['Major','Year'])['GPA'].max())

# average for GPAs for each Major
print(student_df.groupby(by=['Major'])['GPA'].mean())
print(student_df.groupby(by=['Major'])['GPA'].agg(['count','mean']))
print(student_df.groupby(by=['Major'])['GPA'].
      aggregate(['count','mean']))
print(student_df.groupby(by=['Major'])['GPA'].
      agg([np.mean,np.max]))