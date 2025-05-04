import pandas as pd
import numpy as np
import datetime

student_df = pd.read_csv('./part3/students.csv')
n = datetime.datetime.now()
td1 = pd.Timedelta('1 hours 30 minutes')
print(td1)
td2 = pd.Timedelta(hours=1,minutes=30)
print(td2)
td3 = pd.Timedelta(1,unit='h')
print(td3)
print(td1+td2)
print(type(n-datetime.datetime(2004,10,27)))