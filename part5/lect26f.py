import pandas as pd
import json
students_df = pd.read_csv('./part4/students.csv')
students_df.to_json('students_clearned.json',orient='records')
