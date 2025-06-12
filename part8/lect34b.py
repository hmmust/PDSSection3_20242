import requests

khalid = {"Id":202010,"Name":"Khalid Abdeen",
          "Age":21,"Year":2022,"Major":"DSAI","GPA":2.5}

#add_url = "http://127.0.0.1:8000/student/add/"
add_url="http://172.16.139.24:8000/student/add/"
add_response = requests.post(url=add_url,json=khalid)
print(add_response.text)