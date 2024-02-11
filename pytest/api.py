from pathlib import Path
from fastapi import FastAPI

app = FastAPI()


menu = [
    {   'id': 1,
        'name': 'coffee',
        'price': 2.5
     },
    {
        'id': 2,
        'name': 'cake',
        'price': 10
    },
    {
        'id': 3,
        'name': 'tea',
        'price': 3.2
    },
    {
        'id': 4,
        'name': 'croissant',
        'price': 5.79
    }
]

@app.get("/")
def hello_world_root():
    return {"Hello": "World"}

@app.get("/")
def read_item(item_id: int = Path(..., description="Item description")):
    return {"item_id": item_id}

@app.get('/get-item/{item_id}')
def get_item(
    item_id: int = Path(
        None,
        description="Fill with ID of the item you want to view")):

    search = list(filter(lambda x: x["id"] == item_id, menu))

    if search == []:
        return {'Error': 'Item does not exist'}

    return {'Item': search[0]}


@app.get('/get-by-name')
def get_item(name: Optional[str] = None):

    search = list(filter(lambda x: x["name"] == name, menu))

    if search == []:
        return {'item': 'Does not exist'}

    return {'Item': search[0]} 