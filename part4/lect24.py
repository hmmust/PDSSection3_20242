import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler,normalize

student_df = pd.read_csv('./part4/students.csv')
scaler = MinMaxScaler(feature_range=(0,1))
student_df['gpa_scaled']= scaler.fit_transform(student_df.loc[:,['GPA']])
scaler2 = StandardScaler()
student_df['gpa_scaled2']= scaler2.fit_transform(student_df.loc[:,['GPA']])

student_df['gpa_scaled3']= normalize(student_df.loc[:,['GPA']],axis=0,norm='l2')

print(student_df)
