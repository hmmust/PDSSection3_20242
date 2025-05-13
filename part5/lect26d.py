import pandas as pd
import json

with open('students.json') as file1:
    student_data = json.load(file1)
    
print(pd.DataFrame(student_data))
print(student_data[0]['name'])