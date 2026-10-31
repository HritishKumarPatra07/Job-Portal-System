from sqlalchemy.orm import Session 
from sqlalchemy import or_
from ..Schema.User_Schema import CreateUser,UpdateUser
from ..Model.User_Model import User


def duplicate_number_check(
    data : CreateUser,
    db : Session
):

    number = db.query(User).filter(
        User.number == data.number
    ).first()

    return number


def duplicate_email_check(
    data : CreateUser,
    db : Session
):
    email = db.query(User).filter(
        User.email == data.email
    ).first()

    return email

def get_user_by_email(
    email : str,
    db : Session
):
    user_email = db.query(User).filter(
        User.email == email
    ).first()

    return user_email


def create_user(
    data : CreateUser,
    password : str , 
    db : Session
):

    save_data = User(
        name = data.name,
        age = data.age,
        number = data.number,
        email = data.email,
        password = password
    )

    db.add(save_data)
    db.commit()
    db.refresh(save_data)

    return save_data


def get_users(
    search : str | None ,
    offset : int ,
    limit : int ,
    db : Session
):

    if search:
        user = db.query(User).filter(
            or_(
                User.name.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%"),
                User.number.ilike(f"%{search}%")
            )
         ).offset(offset).limit(limit).all()

    else:
        user = db.query(User).offset(offset).limit(limit).all()  


    return user       


def get_user_by_id(
    user_id : int,
    db: Session
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    return user


def duplicate_email_check_for_update(
    user_id : int,
    data : UpdateUser,
    db : Session
):
    email = db.query(User).filter(
        User.email == data.email,
        User.id != user_id
    ).first()


    return email


def duplicate_number_check_for_update(
    user_id : int,
    data : UpdateUser,
    db : Session
):

    number = db.query(User).filter(
        User.number == data.number,
        User.id != user_id
    ).first()

    return number


def update(
    user_id : int ,
    user_data :dict,
    password : str,
    db : Session
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        return None

    for key , value in user_data.items():

        if key == "password":
            continue

        setattr(user,key,value)

    if password is not None:
        user.password = password


    db.commit()
    db.refresh(user)

    return user       


def delete(
    user : CreateUser,
    db : Session
):
    db.delete(user)
    db.commit()

    return f"User Deleted"