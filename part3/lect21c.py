import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')
courses_df = pd.read_csv('./part3/students_courses.csv')
students_courses_df = pd.merge(student_df,courses_df,
                               on=['Id'])
students_courses_df = pd.merge(student_df,courses_df,
                               on=['Id'],how='left')
print(students_courses_df)