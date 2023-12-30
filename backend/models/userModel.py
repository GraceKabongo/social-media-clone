from pydantic import  EmailStr, Field, BaseModel, validator
from typing import Optional, List

from .Model import Model


class UserModel(Model):
    
    fullname: str = Field(min_length=3, max_length=80, require=True)
    username: str = Field(min_length=3, max_length=80, unique=True)
    email : EmailStr = Field(unique=True, require=True)
    password: str = Field (min_length= 6, max_length= 1024, require=True)
    bio: Optional[str] = None
    picture: Optional[str] = None
    admin: bool = Field(default=False)
    follower: List[str] = []
    following: List[str] = []
    posts: List[str] = []
    
    
    

class UpdateUserModel(BaseModel):
    fullname : Optional[str] = Field(min_length=3, max_length=80)
    bio: str = Field(min_length=2, max_length=180, require=True)



def user_serializer(user) -> dict:
    return {
        'id':str(user["_id"]),
        'fullname':user["fullname"],
        'username':user["username"],
        'email':user["email"],
        'bio' :user["bio"],
        'picture':user["picture"],
        'admin':user["admin"],
        'follower': user["follower"],
        'following': user["following"],
        'post':user["posts"]
    }
