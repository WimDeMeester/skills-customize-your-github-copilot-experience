from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Simple Items API")

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

items: Dict[int, Item] = {}

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    items[item.id] = item
    return item

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = items.get(item_id)
    if item is None:
        return {"error": "Item not found"}
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
