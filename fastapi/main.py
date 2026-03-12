from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import List
import json


# initialize app
app = FastAPI()

# create a helper function. on calling which returns the details of students
def load_data():
    with open ('students.json','r') as f: #json file is opened in read mode
        data = json.load(f)

    return data

@app.get("/")
def hello():
    return{'message':'Student Management System API'}

@app.get("/about")
def about():
    return {'message':'A fully functional API to manage your student records'}

# create an endpoint "View" which will show all the student details
@app.get("/view")
def view():
    data = load_data()
    return data

# to check student detail by his/her student_id.
# student_id at path params is passed to function. All student details are fetched from json. 
# check whether chosen student_id is present in json or not. if yes then return it

#### The Path() function in FastAPI is used to provide metadata, validation rules, and documentation hints for path parameters api endpoints.
## we can add : Titles, Description and other constraints and validations. 

@app.get("/student/{student_id}")
def view_student(student_id: str = Path(..., description='ID of the student in the DB', example='S001')):
    # load all the students
    data = load_data()

    if student_id in data:
        student_data = data[student_id]
        return student_data
    return {'message':'error ! student not found'}

#### The Path() function in FastAPI is used to provide metadata, validation rules, and documentation hints for path parameters api endpoints.
## we can add : Titles, Description and other constraints and validations. 

        
