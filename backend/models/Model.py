from typing import Annotated, Optional
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime




class Model(BaseModel):

    created_at: str = Field(default=str(datetime.now()))
    updated_at: str = Field(default= str(datetime.now()))
    