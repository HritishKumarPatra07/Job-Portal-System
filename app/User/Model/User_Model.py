from ...Config.Database import Base
from sqlalchemy import Column , String , Integer ,DateTime
from datetime import datetime


class User(Base):

    __tablename__ = "User"

    id = Column(Integer,primary_key=True,autoincrement=True)
    name =  Column(String(100),nullable=False)
    age = Column(Integer,nullable=False)
    number = Column(String(15),nullable=False,unique=True)
    email = Column(String(100),nullable=False, unique=True)
    password = Column(String(200),nullable=False)
    role = Column(String(100),nullable=False,default="candidate")
    create_at = Column(DateTime , default=datetime.now)
