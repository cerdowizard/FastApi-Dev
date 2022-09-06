from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class BaseUser(BaseModel):
    first_name: str = Field(example="Test")
    last_name: str = Field(example="user")
    username: str = Field(example="testuser")
    email: EmailStr = Field(example="example@gmail.com")
    dob: str = Field(example="20-03-2015")
    phone_number: str = Field(example="07031164320")
    avater: str = Field(example="http://example.com/img08.png")


class UserSchema(BaseUser):
    cn_password: str = Field(..., example="example@1.")
    password: str = Field(..., example="example@1.")


class UserCreate(BaseUser):
    password: str = Field(..., example="example@1.")


class UserPassword(BaseUser):
    password: str


class UserForgotPassword(BaseModel):
    email: str

    class Config:
        orm_mode = True


class ReturnUser(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
    role: Optional[str] = None
