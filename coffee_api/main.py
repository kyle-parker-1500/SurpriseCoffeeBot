from fastapi import FastAPI
from typing import Optional
from typing import Union 
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# pydantic model -> request validation
class Recipe(BaseModel):
    title: str
    ingredients: str
    instructions: str 
     
# setup database
def get_db():
    # find .db file inside computer file
    connector = sqlite3.connect('recipes.db')
    
    connector.row_factory = sqlite3.Row

    return connector

# create table on startup
def init_db():
    # get db file
    connector = get_db()

    # define sql interaction object
    cursor = connector.cursor()

    # create table for recipes
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            ingredients TEXT,
            instructions TEXT 
        )
        '''
    )
    
    connector.commit()
    connector.close()

# initialize db
init_db()

