import pandas as pd

students_df = pd.read_csv('./part4/students.csv',chunksize=2)
for d in students_df:
    print(d)
#print(next(students_df))
#print(next(students_df))