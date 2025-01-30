from fastapi import FastAPI,Path,HTTPException

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

@app.get("/")
def index():
    return {"name":"First Date"}

@app.get("/get-student/{stu_id}")
def get_student(stu_id: int = Path(..., description="The ID of the Student you want to view",gt=0,lt=13,ge=1)):
    if stu_id not in students:
        raise HTTPException(status_code=404,detail="Student not Found")
    return students[stu_id]
