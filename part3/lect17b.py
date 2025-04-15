import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')
print( student_df['Major'])
print( student_df[['Major','Name']])
print( student_df[0:2])






