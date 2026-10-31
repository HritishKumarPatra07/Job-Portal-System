from fastapi import FastAPI
from app.Config.Database import engine , Base
from app.Job_Categories.Model.Categories_Model import JobCategories
from app.Job_Categories.Route import Categories_Route
from app.User.Route import User_Route

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(Categories_Route.router)
app.include_router(User_Route.router)
