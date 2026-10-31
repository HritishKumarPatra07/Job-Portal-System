from pydantic import BaseModel , Field , EmailStr , ConfigDict , field_validator
from datetime import datetime
import re

class CreateUser(BaseModel):

    name : str = Field(
        min_length = 3, 
        max_length=50
    )

    age : int = Field(
        ge=1 ,
        le=100
    )

    number : str = Field(
   
        pattern= r"^[6-9]\d{9}$"

    )

    email : EmailStr 

    password : str= Field(
        min_length= 8,
        max_length=100,
    )

    @field_validator("password")

    @classmethod
    def validate_paassword(cls,value):
        pattern = (
            r"^(?=.*[a-z])"
            r"(?=.*[A-Z])"
            r"(?=.*\d)"
            r"(?=.*[^A-Za-z0-9]).+$"
        )

        if not re.fullmatch(pattern,value):
            raise ValueError(
                "Password needs lowercase, uppercase, digit and special character"
            )

        return value

class ResponseUser(BaseModel):

    id : int
    name : str
    age : int
    number : int
    email : EmailStr
    role : str
    create_at : datetime

    model_config = ConfigDict(from_attributes=True)


class UpdateUser(BaseModel):

    name : str | None = Field(
        default=None,
        min_length=3,
        max_length=50
    )  

    age : int | None = Field(
        default=None,
        ge=1,
        le=100
    )  

    number : str| None = Field(
        default=None,
        pattern= r"^[6-9]\d{9}$"
    )

    email : EmailStr | None = None

    password : str|None = Field(
        default=None,
        min_length=8,
        max_length=100
    )


    @field_validator("password")

    @classmethod
    def validate_password(cls,value):
        pattern = (
            r"^(?=.*[a-z])"
            r"(?=.*[A-Z])"
            r"(?=.*\d)"
            r"(?=.*[^A-Za-z0-9]).+$"
        ) 

        if value is None:
            return value

        elif not re.fullmatch(pattern,value):
            raise ValueError(
                 "Password needs lowercase, uppercase, digit and special character"
            ) 

        return value


class LoginUser(BaseModel):
    email : EmailStr
    password : str = Field(
        min_length=8,
        max_length=100
    )    

    @field_validator("password")

    @classmethod
    def validate_password(cls,value):
        pattern = (
            r"^(?=.*[a-z])"
            r"(?=.*[A-Z])"
            r"(?=.*\d)"
            r"(?=.*[^A-Za-z0-9]).+$"            
        )

        if not re.fullmatch(pattern,value):
            raise ValueError(
                "Password needs lowercase, uppercase, digit and special character"
            )

        return value