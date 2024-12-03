from fastapi import FastAPI

app=FastAPI()

@app.get("/hi/{name}")
async def hello(name):
    return "Hello: " + name + ": Welcome to FastApi Class"