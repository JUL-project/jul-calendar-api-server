from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    user_nid: int


class User(UserBase):
    user_id: str
    password: str
    linked_account_nid: Optional[int] = None
    use_yn: str

    class Config:
        orm_mode = True
