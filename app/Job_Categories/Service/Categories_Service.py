from sqlalchemy.orm import Session
from ..Schema.Categories_Schema import CreateCategoris
from fastapi import HTTPException
from ..DB import Categories_DB



def validate_name(
    data : CreateCategoris,
    db : Session   
):

    if data.Name == "":
        raise HTTPException(
            status_code = 400,
            detail = "Please Enter Your Name"
        )

    if len(data.Name) < 3 or len(data.Name) > 100 :
        raise HTTPException(
            status_code = 400 ,
            detail="Please Enter Valid Name - Min 3 and Max 100"
        )

    existing_name = Categories_DB.duplicate_name(
        data.Name,
        db
    )

    if existing_name is not None:
        raise HTTPException(
            status_code=400,
            detail="Name Already Exist "
        )


    return True


def create_category(
    data : CreateCategoris,
    db : Session
):

    validate_name(
        data,
        db
    )

    return Categories_DB.create_category(
        data,
        db
    )


def get_all_categories(
    search : str | None,    
    page : int,
    limit : int,   
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

    offset = (page -1) * limit

    get_all = Categories_DB.get_all_categories(
        search,
        offset,
        limit,
        db
    )

    if not get_all : 
        raise HTTPException(
            status_code=404,
            detail="Categories Not Found"
        )

    return get_all




def get_category_by_id(
    category_id : int ,
    db : Session
):

    get_category = Categories_DB.get_category_by_id(
        category_id,
        db
    )

    if get_category is None:
        raise HTTPException(
            status_code=404,
            detail="Category Not Found"
        )

    return get_category


def update(
    category_id : int ,
    data : CreateCategoris,
    db : Session
):

    check_category_exist = Categories_DB.get_category_by_id(
        category_id,
        db
    )

    if check_category_exist is None:
        raise HTTPException(
            status_code=404,
            detail="Category Not Found"
        )

    check_duplicate_category = Categories_DB.check_duplicate_category_for_update(
        category_id,
        data,
        db
    )

    if check_duplicate_category is not None:
        raise HTTPException(
            status_code=409,
            detail="Category Name Already Exists"
        )


    return Categories_DB.update(
        check_category_exist,
        data,
        db
    )

    
def delete(
    category_id : int,
    db : Session
):

    check_category_exist = Categories_DB.get_category_by_id(
        category_id,
        db
    )

    if check_category_exist is None:
        raise HTTPException(
            status_code=404,
            detail="Category Not Found"
        )

    return Categories_DB.delete(
        check_category_exist,
        db
    )
    
    