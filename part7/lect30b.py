import requests
import pandas as pd
students = requests.get(url="https://raw.githubusercontent.com/hmmust/PDSSection3_20242/refs/heads/main/students_clearned.json")
#print(type(google.json()))
#Url is correct
if students:
    df = pd.DataFrame(students.json())
    print(df)
else:
    print("Json file is not found!")


