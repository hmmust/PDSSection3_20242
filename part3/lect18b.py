import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')

print(student_df.count())
print(student_df.min())
print(student_df.loc[:,['Age','Year','GPA']].mean())
print(student_df.loc[:,['Age','Year','GPA']].median())
print(student_df.loc[:,['Age','Year','GPA']].cumsum())

max_gpa = student_df['GPA'].max()
print(max_gpa)
year_count = student_df.Year.count()
print(year_count)


