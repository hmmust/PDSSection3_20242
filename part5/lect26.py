import pandas as pd
import json
mira = {'name':'Mira','age':20,
        'courses':('PDS','DB','NW'),
        'passportNo':None}
print(json.dumps(mira))