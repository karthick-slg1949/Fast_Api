from fastapi import FastAPI

app=FastAPI()

@app.get("/book/default")
async def book():
    return "Python Programming"

@app.get("/book/{book_name}")
async def hello(book_name):
    return book_name