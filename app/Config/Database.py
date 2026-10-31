from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker , declarative_base

DATABASE_USER = "root"
DATABASE_PASSWORD = "root"
DATABASE_HOST = "host.docker.internal"
DATABASE_PORT = "3306"
DATABASE_NAME = "job_portal"


DATABASE_URL = (
    f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

engine = create_engine(DATABASE_URL)

LocalSession = sessionmaker(bind=engine)

Base = declarative_base()
    

def get_db():

    db = LocalSession()

    try :
        yield db

    finally:

        db.close()    

