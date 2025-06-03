import pandas as pd
import numpy as np

student_df = pd.read_csv('./part3/students.csv')
#print(list(set(student_df.Major)))
print(list(student_df.Major.unique()))
stno = 20229
student= student_df[student_df.Id == stno]
print(student.size)
print(student.shape[0])
print(len(student))

major = 'DS'
student= student_df[student_df.Major == major]
print(len(student))