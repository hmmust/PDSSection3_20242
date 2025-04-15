import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')
student_df2= student_df.sort_index(axis=1)
student_df.sort_index(axis=1, inplace=True)
student_df.sort_values(by=['Age','Name'], inplace=True)
student_df.sort_values(by=['Age','Name'], 
                       inplace=True,ascending=False)
print(student_df)




