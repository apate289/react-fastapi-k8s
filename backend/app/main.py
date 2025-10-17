from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="Sample FastAPI Backend")

class ItemIn(BaseModel):
    name: str
    description: Optional[str] = None

class ItemOut(ItemIn):
    id: int

# in-memory store for demo
_db = {}
_counter = 1

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/items', response_model=ItemOut)
def create_item(item: ItemIn):
    global _counter
    item_id = _counter
    _counter += 1
    _db[item_id] = item.dict()
    return ItemOut(id=item_id, **_db[item_id])

@app.get('/items', response_model=List[ItemOut])
def list_items():
    return [ItemOut(id=i, **v) for i, v in _db.items()]

@app.get('/items/{item_id}', response_model=ItemOut)
def get_item(item_id: int):
    if item_id not in _db:
        raise HTTPException(status_code=404, detail='Not found')
    return ItemOut(id=item_id, **_db[item_id])
