import pandas as pd
import json
students= [
        {'name':'Mira','age':20,
        'courses':('PDS','DB','NW'),
        'passportNo':None},
         {'name':'Bryhan','age':19,
        'courses':('PDS','ENG'),
        'passportNo':1212121 }          
        ]
print(json.dumps(students))
fh = open('students.json','w')
json.dump(students,fh)
fh.close()

with open('students.json','w') as fh:
        json.dump(students,fh)