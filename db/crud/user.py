import logging

from sqlalchemy.orm import Session

from ..models import user as model
from ..schemas import user as schema


def get_user(db: Session, user_nid: int):
    user = db.query(model.User).filter(model.User.user_nid == user_nid).first()
    return user
