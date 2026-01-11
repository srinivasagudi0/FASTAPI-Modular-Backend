from fastapi import APIRouter, Depends, status , HTTPException
from .. import schemas, models, database
from typing import List
from sqlalchemy.orm import Session, joinedload
from ..repository import blog as blog_repo

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)
get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    # eager-load the creator relationship to include user info with each blog
    blogs = blog_repo.get_all(db)
    return blogs


@router.post('/', status_code= status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    blog = blog_repo.create(request, db)
    return blog




@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int,db: Session = Depends(get_db)):
    deleted = blog_repo.delete(db, id)
    return deleted


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def upadate(id:int, request: schemas.Blog, db: Session = Depends(get_db)):
    update_blog = blog_repo.update(request, db, id)
    return update_blog



#@router.get('/blogs', response_model=List[schemas.Blog], tags=['blogs'])
#def all(db: Session = Depends(get_db)):
#    blogs = db.query(models.Blog).all()
#    return blogs

@router.get('/{id}',status_code= 200, response_model=schemas.ShowBlog)
def show(id: int,db: Session = Depends(get_db)):
    showed = blog_repo.show(db, id)
    return showed





