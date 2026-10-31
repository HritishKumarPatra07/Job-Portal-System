from fastapi import APIRouter ,Depends
from sqlalchemy.orm import Session
from ..Schema.User_Schema import CreateUser,ResponseUser,UpdateUser,LoginUser
from ..Service import User_Service
from ...Config.Database import get_db
from ...Utils.auth import current_user


router = APIRouter(
    prefix="/USER",
    tags=["USER SECTION"]
)

@router.post("/",response_model=ResponseUser)
def create_user(
    data : CreateUser,
    db : Session = Depends(get_db)
):
    return User_Service.create_user(
        data,
        db
    )

@router.get("/get_user/",response_model=list[ResponseUser])
def get_users(
    user = Depends(current_user),
    search : str | None = None,
    page : int = 1,
    limit : int = 10,
    db : Session = Depends(get_db)
):

    return User_Service.get_users(
        search,
        page,
        limit,
        db
    )

@router.get("/get_user_by_id/{user_id}",response_model=ResponseUser)
def get_user_by_id(
    user_id : int,
    db : Session = Depends(get_db)
):

    return User_Service.get_user_by_id(
        user_id,
        db
    )

@router.patch("/update/{user_id}",response_model=ResponseUser)
def update(
    user_id : int,
    data : UpdateUser,
    db: Session = Depends(get_db)
):

    return User_Service.update(
        user_id,
        data,
        db
    )

@router.delete("/Delete/{user_id}")
def delete(
    user_id:int,
    db:Session = Depends(get_db)
):

    return User_Service.delete(
        user_id,
        db
    )

@router.post("/login/")
def login_user(
    data : LoginUser,
    db:Session=Depends(get_db)
):

    return User_Service.login_user(
        data,
        db
    )