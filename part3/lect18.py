import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')
student_df.drop([0,1],inplace=True)
student_df.reset_index(inplace=True,drop=True)
student_df.drop(['GPA'],axis=1,inplace=True)
print(student_df)
student_df2= student_df.iloc[0:1,:]
print(student_df2)
student_df3= pd.concat([student_df,student_df2])
student_df3.reset_index(inplace=True,drop=True)
print(student_df3)



