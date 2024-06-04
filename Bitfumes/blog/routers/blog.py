
from fastapi import APIRouter, Depends, HTTPException, status  # Correct import for status
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, models, outh2
from ..database import get_db
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)



# Get all blogs from the database
@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user:schemas.User = Depends(outh2.get_current_user)):
    return blog.get_all(db)
   



# Create a new blog
@router.post('/', response_model=schemas.ShowBlog, status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db),current_user:schemas.User = Depends(outh2.get_current_user)):
    return blog.create(request, db)




# Update a blog
@router.put('/{id}', response_model=schemas.ShowBlog, status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db),current_user:schemas.User = Depends(outh2.get_current_user)):
    return blog.update(id, request, db)

# Delete a blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, responses={404: {"description": "Blog not found"}})
def destroy(id: int, db: Session = Depends(get_db),current_user:schemas.User = Depends(outh2.get_current_user)):
        return blog.destroy(id, db)
   


# Get a specific blog by ID
@router.get('/{id}', response_model=schemas.ShowBlog, status_code=status.HTTP_200_OK)
def show(id: int, db: Session = Depends(get_db),current_user:schemas.User = Depends(outh2.get_current_user)):
     return blog.get_by_id(id, db)
    