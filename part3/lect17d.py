import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')
del student_df['Major']
student_df.pop('GPA')

student_df['BirthYear'] = 2025 - student_df['Age']
student_df['BirthYear'] = pd.Series(
    2025 - student_df['Age'],dtype=np.int32)
student_df['FirstName'] = [ i.split()[0] for i in 
                           student_df['Name']]
print(student_df)



