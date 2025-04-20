import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')
student_df['BirthYear'] = 2025-student_df['Age'] 

print(student_df['Age'].corr(student_df['BirthYear']))
print(student_df['Age'].corr(student_df['GPA']))
print(student_df.loc[:,['Age','Year','BirthYear','GPA']].corr())
print(student_df.loc[:,['Age','Year','BirthYear','GPA']].cov())
#student_df['AgeRank']= student_df['Age'].rank()
student_df['AgeRank']= student_df['Age'].rank(method='dense')
print(student_df)
print(student_df.loc[:,['Age','Year','BirthYear','GPA']].rank())



