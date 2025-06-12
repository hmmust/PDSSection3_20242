from fastapi import FastAPI,HTTPException
import pandas as pd
import numpy as np
import json
from pydantic import BaseModel

app = FastAPI()
student_df = pd.read_csv('../part3/students.csv')

class Student(BaseModel):
    Id: int
    Name:str
    Age:int
    Year:int
    Major:str
    GPA:float

@app.post("/student/add")
def add_student(student:Student):
    new_student = pd.DataFrame([student.dict()])
    new_student_df = pd.concat([student_df,new_student],ignore_index=True)
    new_student_df.to_csv("../part3/students.csv")
    return {"message":"student added!"}