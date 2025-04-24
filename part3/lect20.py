import pandas as pd
import numpy as np
student_df = pd.read_csv('./part3/students.csv')
print(student_df.info())
print(student_df.isnull())
print(student_df.isnull().sum())
print(student_df.notnull().sum())
print(student_df.Year.isnull().sum())
#student_df.Year.fillna(0,inplace=True)
#student_df.Year.fillna(method='pad',inplace=True)
#student_df.Year.fillna(method='backfill',inplace=True)
student_df.Year.fillna(student_df['Year'].median(),inplace=True)
#student_df.Year.fillna(student_df['Year'].mean(),inplace=True)
#student_df.dropna(inplace=True)
#student_df.dropna(axis=1, inplace=True)
student_df.Major=student_df.Major.str.strip()
student_df.Major.replace({"DSS":'DS'}, #' SE':'SE'                      },
                         inplace=True)
#print(student_df.Major.value_counts())
student_df['Year']=student_df['Year'].astype(np.int16)
print(student_df.dtypes)




