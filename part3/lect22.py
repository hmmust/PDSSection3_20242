import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')
courses_df = pd.read_csv('./part3/students_courses.csv')
students_courses_df = pd.concat([student_df,courses_df],axis=1)
print(students_courses_df)
student_df.Year.fillna(student_df['Year'].median(),inplace=True)
student_df['Year']= student_df['Year'].astype(np.int32)
student_df['Year'] = pd.Categorical(student_df['Year'])
print(student_df.dtypes)
print(student_df['Year'].cat.categories)
print(student_df['Year'].cat.codes)