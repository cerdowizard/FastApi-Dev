from pydantic import BaseModel, Field


class ListUser(BaseModel):
    email: str = Field(..., example="name@gmail.com")
    fullname: str = Field(..., example="testUser")
    cn_password: str = Field(..., example='password')


class UserCreate(ListUser):
    password: str = Field(..., example="password")


class UserPassword(BaseModel):
    password: str
