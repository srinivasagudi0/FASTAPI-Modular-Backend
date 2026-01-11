from pydantic import BaseModel, validator
from typing import List


class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List["Blog"]
    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    creator: "ShowUser"
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

    @validator("password")
    def password_max_length(cls, v: str) -> str:
        # bcrypt supports up to 72 bytes; block longer inputs early
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password too long (72-byte bcrypt limit)")
        return v

# resolve forward refs for nested schemas
ShowUser.update_forward_refs()
ShowBlog.update_forward_refs()


class Login(BaseModel):
    username: str
    password: str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None