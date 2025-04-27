import pandas as pd
import numpy as np
import datetime

student_df = pd.read_csv('./part3/students.csv')
n = datetime.datetime.now()
khalid= datetime.datetime(2004,10,27)
print(n,khalid,n-khalid) #timedelta #datespan

print(n.strftime('%c'),n.strftime('%x'),n.strftime('%X'))
print(n.strftime('%Y/%m/%d'))
