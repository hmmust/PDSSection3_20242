from fastapi import FastAPI
app = FastAPI()
@app.get("/") #decorator function
def read_root():
    return {"message": "Hello World"}

@app.get("/khalid") #decorator function
def read_khalid():
    return {"name": "Khalid Abdeen"}

@app.get("/student/{student_name}") #decorator function
def read_student(student_name):
    return {"name": student_name}

@app.get("/student/name/") #decorator function
def read_student_name(stname):
    return {"name": stname}

@app.get("/student/age/{age}") #decorator function
def read_age(age:int):
    return {"name": age}