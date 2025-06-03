import pandas as pd
import numpy as np
import requests

major_url="http://localhost:8000/students/major/DS"
major_url="http://localhost:8000/students/20229"
major_url="http://localhost:8000/students/add"

#results = requests.get(url=major_url) 
#print(results.json())
#print(results.status_code)
student = {"Id": 999,"Name": "Mazen Bassam","Major": "DS",
           "Age":21, "Year":2022, "GPA": 3.8}
results = requests.post(url=major_url,json=student) 
print(results.text)