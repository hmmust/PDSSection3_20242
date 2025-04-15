import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')
print( student_df.loc[0,'Age']) # [index, columnname]
print( student_df.loc[0:3,['Name','Age']]) 
print( student_df.iloc[0:3,[1,3]]) # [row num, col num]
print( student_df.iloc[[0,1],[1,3]]) # [row num, col num]

print( student_df.iloc[:,0:-1]) # All rows, all columns except last
print( student_df.iloc[:,[0,1,3,4]]) 







