import requests
import pandas as pd
students = requests.post(url="http://httpbin.org/post",json={
    "key":"Khalid Abdeen"
})
if students:
    print(students.json())
    print(students.json()['origin'])
else:
    print("Json file is not found!")


