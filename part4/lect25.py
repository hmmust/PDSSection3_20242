import pandas as pd
import numpy as np
from sklearn.preprocessing import Binarizer,LabelEncoder

student_df = pd.read_csv('./part4/students.csv')
bin = Binarizer(threshold=3)
student_df['gpa_bin']= bin.fit_transform(student_df.loc[:,['GPA']])

student_df['Major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)

label_enc = LabelEncoder()
label_enc.fit(['CS', 'DS', 'IS', 'SE','VR'])

student_df['Major_enc']= label_enc.fit_transform(student_df['Major'])

print(student_df)
