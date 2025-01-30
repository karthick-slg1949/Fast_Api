from fastapi import FastAPI,HTTPException,Path,Query
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

students={
    1:{
        "name":"karthick",
        "age":23,
        "City":"SVG"
    },
    2:{
        "name":"Dinesh",
        "age":18,
        "City":"SLG"
    },
    3:{
        "name":"Katuscha",
        "age":18,
        "city":"Girona"
        },
    4:{
        "name":"Charles",
        "age":35,
        "city":"Columbus"
        },
    5:{
        "name":"Edith",
        "age":38,
        "city":"Loimaan Kunta"
        },
    6:{
        "name":"Mariya",
        "age":41,
        "city":"Matanza"
        },
    7:{
        "name":"Shamus",
        "age":50,
        "city":"Chigasaki"
        },
    8:{
        "name":"Roselia",
        "age":24,
        "city":"Vesele"
        },
    9:{
        "name":"Talya",
        "age":20,
        "city":"Ust-Kalmanka"
        },
    10:{
        "name":"Arlin",
        "age":24,
        "city":"Zadawa"
        },
    11:{
        "name":"Ervin",
        "age":28,
        "city":"Maguwon"
        },
    12:{
        "name":"Hillary",
        "age":38,
        "city":"Caucasia"
        }
}

class student(BaseModel):
    name:str
    age:int
    city:int

@app.get("/")
def index():
    return {"Name":"First Name"}

@app.get("/get-student_id/{stu_id}")
def get_student(stu_id : int = Path(...,description="The Id of the Student you want to view",gt=0,lt=20,ge=1)):
    if stu_id not in students:
        raise HTTPException(status_code=404,detail="Student Not Found")
    return students[stu_id]

@app.get("/get-by-name/{stu_id}")
def get_student(*,stu_id : int,name : Optional[str]=None,test:int):
    for stu_id in students:
        if students[stu_id]['name']==name:
            return students[stu_id]
    return {"Data Not Found"}

@app.post("/create-student/{stu_id}")
def create_student(stu_id : int, student : student):
    if stu_id in students:
        return {"Error":"student Exists"}
    students[stu_id]=student
    return students[stu_id]
# get-by-name?name=karthick