import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')
#student_df['Name']= [ i.lower() for i in student_df['Name']]
student_df['Email']= student_df['Name'].str.lower().str.replace(" ","")
print(student_df)



