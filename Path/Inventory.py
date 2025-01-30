from fastapi import FastAPI, Path
from typing import Optional

app=FastAPI()

inventory={
    1:{
        "name":"Milk",
        "Price":100,
        "Brand":"Avin"
    },
    2:{
        "name":"Biscuit",
        "Price":170,
        "Brand":"Britannia"
    }
}
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., description="The id of the item you'd like",gt=0,lt=3)):
    return inventory[item_id]

@app.get("/get-by-name/{item_id}")
def get_item(*, item_id :int,name : Optional [str] = None, test :int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data" :"Not Found"}