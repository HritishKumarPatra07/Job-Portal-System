from sqlalchemy.orm import Session 
from ..Model.Categories_Model import JobCategories
from sqlalchemy import func
from ..Schema.Categories_Schema import CreateCategoris


def duplicate_name(
   name : str,
   db : Session
):

    get_name = db.query(JobCategories).filter(
        func.lower(func.replace(JobCategories.Name, " ",""))
        == name.replace(" ","").lower()
    ).first()

    return get_name


def create_category(
    data : CreateCategoris,
    db : Session   
):
    save_data = JobCategories(
        Name = data.Name
    )

    db.add(save_data)
    db.commit()
    db.refresh(save_data)

    return save_data


def get_all_categories(
        search : str | None,
        offset : int,
        limit : int,
        db : Session
    ):

    if search:
        search = search.strip()

        get_all = db.query(JobCategories).filter(
            JobCategories.Name.ilike(f"%{search}%")
        ).offset(offset).limit(limit).all()
    else:    
       get_all = db.query(JobCategories).offset(offset).limit(limit).all()

    return get_all



def get_category_by_id(
    category_id : int ,
    db : Session
):

    get_category = db.query(JobCategories).filter(
        JobCategories.id == category_id
    ).first()

    return get_category


def check_duplicate_category_for_update(
    category_id : int ,
    data :  CreateCategoris,
    db : Session
):

    check_duplicate = db.query(JobCategories).filter(
        func.lower(func.replace(JobCategories.Name," ",""))
        == data.Name.replace(" ","").lower() ,
        JobCategories.id != category_id
    ).first()

    return check_duplicate


def update(
    category : JobCategories,    
    data : CreateCategoris,
    db : Session
):
    category.Name = data.Name

    db.commit()
    db.refresh(category)

    return  category


def delete(
    category : JobCategories ,
    db : Session
):

    db.delete(category)
    db.commit()

    return {
        "message" : {

            "Category Deleted Successfully"

        }
    }

    