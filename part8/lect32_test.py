import pandas as pd
import numpy as np

student_df = pd.read_csv('./part3/students.csv')
#print(list(set(student_df.Major)))
print(list(student_df.Major.unique()))