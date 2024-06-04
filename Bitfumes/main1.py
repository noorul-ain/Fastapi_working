from typing import Union

from fastapi import FastAPI
from typing  import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get("/")  #base path
def index():
    return {'daata':'Blog list'}


@app.get("/blog/unpublishedblog")
def comments(id):
    # fetceh blog with id = id
    return {'data':'unpublished blog comments'}


@app.get("/blog/{id}")    
def xyz(id):
    # fetceh blog with id = id
    return {'data':id}


@app.get("/blog/{id}/comments")
def comments(id):
    # fetceh blog with id = id
    return {'data':{'commenat1','comment2','comment3'}}

# -----Query parameters --------------------------------
@app.get("/query")
def que():  #http://127.0.0.1:8000/query?limit=10
    # fetceh blog with id = id
    return {'data':'blog list'}

@app.get("/queryparameter")
def que(limit): 
     #http://127.0.0.1:8000/queryparameter?limit=10

    # 10 published blog
    return {'data':f'{limit}blog list'}

@app.get("/queryTrue")
def que(limit,published:bool):  
    # http://127.0.0.1:8000/queryTrue?limit=50&published=true

    if published: 
        return {'data':f'{limit}blog list from db'}
    else:
        return {'data':f'{limit}blog list'}
    
@app.get("/querysort")
def que(limit= 10 , published:bool =True , sort:Optional[str]=None):  

    if published: 
        return {'data':f'{limit}blog list from db'}
    else:
        return {'data':f'{limit}blog list'}
    

    # ==========Request body=========


class Blog(BaseModel):
    name: str
    body :str
    Published : Optional[bool]


@app.post("/items/")
async def create_item(blog: Blog):
    return blog
     # =================Debugging=====================
    #  ctrl shift p
    #  =================Pydantic Schemas==============
    # =============Database Connection=============