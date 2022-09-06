from sqlalchemy import Boolean, Column, String, Integer, Enum, DateTime, func, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from api.utils.base import Base


class Roles(str, enum.Enum):
    Admin = "admin"
    User = "user"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(101), nullable=False)
    last_name = Column(String(101), nullable=False)
    username = Column(String(101), unique=True, nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    dob = Column(String(101), nullable=False)
    phone_number = Column(String(101), nullable=False)
    avater = Column(String(255))
    password = Column(String(101), nullable=False)
    is_active = Column(Boolean(), default=True)
    role = Column(Enum(Roles), default=Roles.User)
    created_at = Column(DateTime(), default=func.now())
    posts = relationship("Post", back_populates="owner", cascade="all,delete")
    updated_at = Column(DateTime(), onupdate=datetime.now())


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(101), nullable=False, unique=True, index=True)
    short_desc = Column(String(101), nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String(101), nullable=False)
    imageUrl = Column(String(101), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="posts")
    created_at = Column(DateTime(), default=func.now())
    updated_at = Column(DateTime(), onupdate=datetime.now())


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(101), nullable=False, unique=True, index=True)
    created_at = Column(DateTime(), default=func.now())
    updated_at = Column(DateTime(), onupdate=datetime.now())


class Token(Base):
    __tablename__ = "rest_code"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(101), nullable=False, unique=True, index=True)
    rest_code = Column(String(101))
    expire_in = Column(DateTime)
    created_at = Column(DateTime(), default=func.now())
