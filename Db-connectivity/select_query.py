from sqlalchemy import select
from sqlalchemy.orm import Session
from connect import engine
from models import Base, User, Address


session = Session(engine)

stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

# for user in session.scalars(stmt):  #scaer mean query ko execute karna
#     print(user)

users = session.query(User).all()
for user in users:
    print(user)
