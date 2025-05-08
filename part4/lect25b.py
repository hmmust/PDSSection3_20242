import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

student_df = pd.read_csv('./part4/students.csv')
student_df['Major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)

ohe = OneHotEncoder()
encoded_data = ohe.fit_transform(student_df[['Major']])
#print(encoded_data)
#print(ohe.get_feature_names_out(['Major']))
student_df_enc = pd.DataFrame(
    encoded_data.toarray(),
    columns=ohe.get_feature_names_out(['Major']))
print(student_df_enc)
