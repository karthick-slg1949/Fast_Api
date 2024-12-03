from fastapi import FastAPI

app=FastAPI()

@app.get("/book")
async def books(limit : int):
    a = [
        {"1001" : "Python"},
        {"1002" : "CSS"},
        {"1003" : "HTML"},
        {"1004" : "Javascript"},
        {"1005" : "React JS"},
        {"1006" : "Node JS"},
        {"1007" : "Bootstrap"},
        { "1008" : "Express JS"},
        { "1009" : "Fast Api"},
        { "1010" : "GitHub"}
    ]
    return {"Book Data is : {}".format(a[:limit])}