

# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from .. import schemas, database, models,token
# from ..database import get_db
# from ..hashing import Hash  # Assuming you have a hashing module for password verification
# from ..token import create_access_token  # Assuming you have a module for token creation
# from fastapi.security import  OAuth2PasswordRequestForm

# router = APIRouter(
#     tags=["Authentication"],
# )

# @router.post('/login')
# def login(form_data: OAuth2PasswordRequestForm, db: Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.email == form_data.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
#     if not Hash.verify(user.password, request.password):  # Assuming you have a verify method in Hash class
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
#         # Genrate Jwt token
#     access_token = token.create_access_token(data={"sub": user.email})  # Assuming `sub` is used for subject (user identifier)
#     return {"access_token": access_token, "token_type": "bearer"}
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models, token
from ..database import get_db
from ..hashing import Hash  # Assuming you have a hashing module for password verification
from ..token import create_access_token  # Assuming you have a module for token creation
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=["Authentication"],
)

@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if not Hash.verify(form_data.password, user.password):  # Corrected password verification
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
