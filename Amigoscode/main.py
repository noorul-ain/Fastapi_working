from fastapi import FastAPI,HTTPException
from uuid import uuid4 ,UUID
from typing import List
from models import User,Gender,Role,UserUpdateRequest

app = FastAPI()



db: List[User] = [
    User(
        id=uuid4(),
        first_name="Aex",
        last_name="Doe",
        middle_name=None,
        gender=Gender.male,
        roles=[Role.user, Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Jamila",
        last_name="Ahmad",
        middle_name=None,
        gender=Gender.female,
        roles=[Role.user, Role.student]
    )
]
#Get method req a representation of the specified resource.Req using GET shuld ony retrive data

@app.get("/api/users")
async def fetch_users():
    return db

# The postmethod submits an entity to the specified resource,often causing a change instate or side effect on the server
# submit a new usr
@app.post("/api/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

# The delete method delete the specified resources
@app.delete("/api/users{user_id}")
async def delete_user(user_id = UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
        raise HTTPException(status_code=404, detail=f"User with id:{user_id} dos not exists")
    
@app.put("/api/users{user_id}")
async def update_user(user_update:UserUpdateRequest,user_id = UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return 
    raise HTTPException(status_code=404, detail=f"User with id:{user_id} dos not exists")
            
            
