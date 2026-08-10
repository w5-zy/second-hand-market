from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserResp(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class GoodsCreate(BaseModel):
    title: str
    price: int
    desc: str

class GoodsResp(GoodsCreate):
    id: int
    user_id: int
    class Config:
        orm_mode = True
