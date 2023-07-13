from sqlalchemy import Column, Integer, String, DateTime

from ..database import Base


class User(Base):
    __tablename__ = "user"

    user_nid = Column(Integer, primary_key=True)
    user_id = Column(String(20))
    password = Column(String)
    linked_account_nid = Column(Integer, nullable=True)
    use_yn = Column(String(2))
    create_dtm = Column(DateTime)
    update_dtm = Column(DateTime, nullable=True)
