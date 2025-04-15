import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')
print(student_df[ student_df['Major'] == 'DS'  ])
print(student_df[ student_df['Major'].isin(['DS','IS'])  ])
print(student_df[ (student_df['Major'] == 'DS') &
                 (student_df['GPA'] >3)  ])
print(student_df[~( student_df['Major'] == 'DS')])



