from fastapi import FastAPI

app=FastAPI()

@app.get("/book/{book_id}")
async def book(book_id):
    Book_Data ={
        "1001" : "Python",
        "1002" : "CSS",
        "1003" : "HTML",
        "1004" : "Javascript",
        "1005" : "React JS",
        "1006" : "Node JS",
        "1007" : "Bootstrap",
        "1008" : "Express JS",
        "1009" : "Fast Api",
        "1010" : "GitHub"
    }
    return {"Book ID : {} and Book Name : {}".format(book_id, Book_Data[book_id])}