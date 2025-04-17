import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')
student_df['BirthYear'] = 2025-student_df['Age'] 

print(student_df['Age'].corr(student_df['BirthYear']))
print(student_df['Age'].corr(student_df['GPA']))




