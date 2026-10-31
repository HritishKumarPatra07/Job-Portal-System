from sqlalchemy.orm import Session
from ..Schema.User_Schema import CreateUser,UpdateUser,LoginUser
from ..DB import User_DB
from fastapi import HTTPException
from ...Utils.password import hashpassword,varify_password
from ...Utils.JWT import create_token


def create_user(
    data : CreateUser,
    db : Session
):

    check_number_existing = User_DB.duplicate_number_check(
        data,
        db
    )

    if check_number_existing is not None:
        raise HTTPException(
            status_code=409,
            detail="Phone number already registered"
        )


    check_email_existing = User_DB.duplicate_email_check(
        data,
        db
    )

    if check_email_existing is not None:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    password = hashpassword(data.password)


    return User_DB.create_user(
        data,
        password,
        db
    )


def get_users(
    search : str | None,
    page : int ,
    limit : int ,
    db : Session
):
    if page < 1 :
        raise HTTPException(
            status_code=400,
            detail="Page must be greater than 0"
        )

    if limit < 1 :
        raise HTTPException(
            status_code=400,
            detail="Limit must be greater than 0"
        )

    offset = (page-1) * limit

    users  = User_DB.get_users(
        search,
        offset,
        limit,
        db
    )

    if not users:
        raise HTTPException(
            status_code=404,
            detail="users not found"
        )

    return users


def get_user_by_id(
    user_id : int,
    db : Session
):

    user = User_DB.get_user_by_id(
        user_id,
        db
    )
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )

    return user



def update(
    user_id : int,
    data : UpdateUser,
    db : Session     
):

    check_user_existing = User_DB.get_user_by_id(
        user_id,
        db
    )
    if check_user_existing is None:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    if data.email is not None:   
        check_email_duplicate = User_DB.duplicate_email_check_for_update(
            user_id,
            data,
            db
         )

        if check_email_duplicate is not None:
            raise HTTPException(
                status_code=409,
                detail="Email already registered"
            )

    if data.number  is not None:

        check_number_duplicate = User_DB.duplicate_number_check_for_update(
            user_id,
            data,
            db
        )

        if check_number_duplicate is not  None:
            raise HTTPException(
                status_code=409,
                detail="Number already registered"
            )

    if data.password is  None:
        password = None
    else:
       password = hashpassword(data.password)

    update_data = data.model_dump(exclude_unset=True)   

    return User_DB.update(
        user_id,
        update_data,
        password,
        db
    )

def delete(
    user_id:int,
    db : Session
):

    user = User_DB.get_user_by_id(
        user_id,
        db
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    return User_DB.delete(
        user,
        db
    )

def login_user(
    data : LoginUser,
    db: Session
):

    user_email = User_DB.get_user_by_email(
        data.email,
        db 
    )

    if user_email is None:
        raise HTTPException(
            status_code=404,
            detail="Invalid Email & Password"
        )

    varify_pass = varify_password(
        data.password,
        user_email.password
    )

    if varify_pass is False:
        raise HTTPException(
            status_code=404,
            detail="Invalid Email & Password"      
    )

    token = create_token(
        user_email.id,
        user_email.role
    )

    return {
        "Access_Token":token,
        "token_type": "bearer"
    }


    

    