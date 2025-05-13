import pandas as pd
import json
json1= '[{"name": "Mira", "age": 20, "courses": ["PDS", "DB", "NW"], "passportNo": null}, {"name": "Bryhan", "age": 19, "courses": ["PDS", "ENG"], "passportNo": 1212121}]'
json2= '{"name": "Mira", "age": 20, "courses": ["PDS", "DB", "NW"], "passportNo": null}'
obj1= json.loads(json1)
obj2= json.loads(json2)

print(type(obj1),type(obj2))
print(obj1[0],obj2['name'])