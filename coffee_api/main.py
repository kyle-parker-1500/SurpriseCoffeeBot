from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    
@app.get('/')
async def home():
    await print("Hello World")