from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, models, database
from typing import List
from sqlalchemy.orm import Session
from ..repository.user import create, get_user as repo_get_user

router = APIRouter(
    prefix="/user",
    tags=["users"]
)

get_db = database.get_db


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def read_user(id: int, db: Session = Depends(get_db)):
    user = repo_get_user(db, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
