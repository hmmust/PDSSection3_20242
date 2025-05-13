import pandas as pd
import json
students_df = pd.read_json('students.json')
students_df.age = students_df.age + 1

students_df.to_json('students_clearned.json',orient='records')
