from fastapi import APIRouter , Depends
from ..Schema.Categories_Schema import CreateCategoris , ResponseCategories
from sqlalchemy.orm import Session
from ...Config.Database import get_db
from ..Service import Categories_Service

router = APIRouter(
    prefix="/CATEGORY",
    tags=["CATEGORY SECTION"]
)


@router.post("/",response_model=ResponseCategories)
def create_category(
    data : CreateCategoris,
    db : Session = Depends(get_db)
):

    return Categories_Service.create_category(
        data,
        db
    ) 

@router.get("/get_cateories/",response_model=list[ResponseCategories])
def get_all_categories(
    search : str | None = None,
    page : int = 1,
    limit : int = 10,
    db : Session = Depends(get_db)
):

    return Categories_Service.get_all_categories(
        search,                 
        page,
        limit,
        db
    )




@router.get("/get_category_by_id/{category_id}",response_model=ResponseCategories)
def get_category_by_id(
    category_id : int,
    db : Session = Depends(get_db)

):
   return Categories_Service.get_category_by_id(
       category_id,
       db
   )
    

@router.patch("/update/{category_id}")
def update(
    category_id : int,
    data : CreateCategoris,
    db : Session = Depends(get_db)
):

    return Categories_Service.update(
        category_id,
        data,
        db
    )

@router.delete("/delete/{category_id}")
def delete(
    category_id : int,
    db : Session = Depends(get_db)
):
    
    return Categories_Service.delete(
        category_id,
        db
    )