from pydantic import BaseModel,Field,ConfigDict
from datetime import datetime

class CreateCategoris(BaseModel):

    Name : str = Field(
     min_length=3 ,
     max_length=100)

class ResponseCategories(BaseModel):

    id : int
    Name : str
    created_at : datetime

    model_config = ConfigDict(from_attributes=True)



