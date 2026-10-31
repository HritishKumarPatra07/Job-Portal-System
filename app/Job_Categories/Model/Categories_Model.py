from sqlalchemy import Column , String , Integer , DateTime 
from ...Config.Database import Base
from datetime import datetime

class JobCategories(Base):

    __tablename__ = "job_categories"

    id = Column(Integer,primary_key=True,autoincrement=True)
    Name = Column(String(100), nullable=False)
    created_at = Column(DateTime,default=datetime.now)