from pydantic import BaseModel
from typing import List, Optional, Union

# defing a class for response model 
# it is the reporesentation of the data that is sent back to the client


class User(BaseModel):
    username : str
    email : Union[str, None] = None
    password : str
    disabled: Union[bool, None] = None

    class Config():
        orm_mode = True

class User_get(BaseModel):
    username : str
    email : Union[str, None] = None
    disabled: Union[bool, None] = None

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    username : str
    email : str

    class Config():
        orm_mode = True

class Login(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    username : Optional[str] = None