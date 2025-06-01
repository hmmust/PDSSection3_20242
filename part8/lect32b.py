from fastapi import FastAPI
import pandas as pd
import numpy as np
app = FastAPI()

import pandas as pd
import numpy as np

student_df = pd.read_csv('../part3/students.csv')

@app.get("/majors") #decorator function
def read_majors():
    return list(student_df.Major.unique())
