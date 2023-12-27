from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional, List

from pydantic.functional_validators import BeforeValidator


PyObjectId = Annotated[str, BeforeValidator(str)]

class UserModel(BaseModel):
    
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(min_length=3, max_length=80,require=True)
    surname: str = Field(min_length=3, max_length=8,require=True)
    username: str = Field(min_length=3, max_length=80, unique=True,require=True)
    email : EmailStr = Field(unique=True, require=True)
    password: str = Field (min_length= 6, max_length= 1024, require=True)
    bio: Optional[str]
    follower: List[str]
    following: List[str]
    posts: List[str]
    