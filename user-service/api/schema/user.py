from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    userid: str
    name: str
    email: str

    class Config:
        from_attributes=True


class UserLogin(BaseModel):
    userid: str
    passwd: str


class UserCreate(UserBase):
    passwd: str


class User(UserBase):
    mno: int
    regdate: str


class Token(BaseModel):
    access_token: str
    token_type: str


