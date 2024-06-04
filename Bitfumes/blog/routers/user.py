

from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..database import get_db
from ..repository import user




router = APIRouter(
     prefix="/user",
    tags=["Users"],
)

# Create User
@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
   return user.create_user(request, db)




# Show User
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
   return user.show(id,db)
