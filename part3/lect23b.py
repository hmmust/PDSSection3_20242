import pandas as pd
import numpy as np
import datetime
student_df = pd.read_csv('./part3/students.csv')
n = datetime.datetime.now()
td1 = pd.Timedelta(hours=1,minutes=15)

print(pd.date_range('5/4/2025 8:00', periods=5,freq='30min'))
print(pd.date_range('5/4/2025 8:00', periods=6,freq='1h'))
print(pd.date_range('5/4/2025 8:00', periods=6,freq=td1))
print(pd.date_range('5/4/2025 8:00', periods=6,freq=td1))
print(pd.date_range('5/4/2025 8:00', '5/4/2025 12:00',periods=15))
student_df['project_d']= pd.date_range('5/4/2025 9:00', periods=12,freq='15min')
student_df['project_d']=student_df['project_d']+pd.Timedelta(45,unit='minute')
print(student_df)
