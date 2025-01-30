from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def hello():
    return {"Data" : "Test"}

@app.get("/about")
def about():
    return{"Data" : "About"}