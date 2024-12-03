from fastapi import FastAPI

app=FastAPI()

@app.get("/book/{book_id}/{book_name}")
async def hello(book_id : int, book_name):
    return "Book Id: " + str(book_id) + " : Book Name: " + book_name 