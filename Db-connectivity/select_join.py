from sqlalchemy.orm import Session
from connect import engine
from models import Base, User, Address
from sqlalchemy import select


session = Session(engine) #connection 


stmt = (
    select(Address)
    .join(Address.user)
    .where(User.name == "sandy")
    .where(Address.email_address == "sandy@sqlalchemy.org")
)
user = session.scalars(stmt).one()
print(user)
