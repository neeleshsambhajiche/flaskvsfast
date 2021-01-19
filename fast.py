from fastapi import FastAPI
from pydantic import BaseModel
import aiohttp
from typing import List

app = FastAPI()

conn = aiohttp.TCPConnector(limit=20)
client_session = aiohttp.ClientSession(connector=conn)


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

class TextSample(BaseModel):
    message: str


class CPU_Job_Response(BaseModel):
    n: int


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/io_job", response_model=TextSample)
async def io_job():
    url = "https://api.github.com"
    async with client_session.get(url) as resp:
        response = await resp.json()

    return response


@app.get("/cpu_job", response_model=CPU_Job_Response)
def cpu_job():
    n = 5000
    while n > 0:
        n -= 1
    respData = {
        "n": n
    }
    return respData



@app.on_event("shutdown")
async def cleanup():
    await client_session.close()