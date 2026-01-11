from fastapi import APIRouter
from .. import schemas, database, models,token
from sqlalchemy.orm import Session
from fastapi import Depends
from ..hashing import Hash
from datetime import datetime,timedelta


router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user  = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        return {'error': 'Invalid Credentials'}
    if not Hash.verify(user.password, request.password):
        return {'error': 'Invalid Credentials'}

    #generate token and return
    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
