from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.models import user as model
from db.crud import user as crud
from db.schemas import user as schema
from db.database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/users",
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{user_nid}", response_model=schema.User)
async def read_user(user_nid: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_nid=user_nid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
