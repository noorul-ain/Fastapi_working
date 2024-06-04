from sqlalchemy import select
from sqlalchemy.orm import Session
from connect import engine
from models import Base, User, Address


session = Session(engine)


stmt = select(User).where(User.name == "patrick")
user = session.scalars(stmt).one()
user.addresses.append(Address(email_address="PPpatrickstar@sqlalchemy.org"))

session.commit()
