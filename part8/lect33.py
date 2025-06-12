from fastapi import FastAPI,HTTPException
import pandas as pd
import numpy as np
import json
from pydantic import BaseModel

app = FastAPI()
class Student(BaseModel):
    Id:int
    Name:str
    Age:int
    Year:int = None
    GPA: float
    Major:str
student_df = pd.read_csv('../part3/students.csv')
@app.get("/students/{stno}") #decorator function
def read_student(stno:int): #string
    #stno=int(stno)
    student= student_df[student_df.Id == stno]
    if len(student)>0:
        return json.loads(student.to_json())
    else:
        raise HTTPException(status_code=404,detail="Student not found!")
        return {"error":"Student not found!"}


@app.get("/students/major/{major}") #decorator function
def read_major_students(major:str): #string
    #stno=int(stno)
    student= student_df[student_df.Major == major]
    if len(student)>0:
        return json.loads(student.to_json(orient="records"))
    else:
        raise HTTPException(status_code=404,detail="Major not found!")

@app.post("/students/add") #decorator function
def add_student(student:Student): #string
    student = student.dict()
    return student