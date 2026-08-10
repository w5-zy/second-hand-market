from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
import models, schemas
from passlib.context import CryptContext

Base.metadata.create_all(bind=engine)
app = FastAPI(title="二手交易API")
pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post("/api/user/register", response_model=schemas.UserResp)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="用户名已存在")
    hash_pwd = pwd_ctx.hash(user.password)
    new_user = models.User(username=user.username, password=hash_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/api/user/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not pwd_ctx.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="账号密码错误")
    return {"uid": db_user.id, "username": db_user.username}

@app.post("/api/goods", response_model=schemas.GoodsResp)
def create_goods(goods: schemas.GoodsCreate, uid: int, db: Session = Depends(get_db)):
    new_goods = models.Goods(**goods.dict(), user_id=uid)
    db.add(new_goods)
    db.commit()
    db.refresh(new_goods)
    return new_goods

@app.get("/api/goods", response_model=list[schemas.GoodsResp])
def get_all_goods(db: Session = Depends(get_db)):
    return db.query(models.Goods).all()

@app.get("/api/goods/me", response_model=list[schemas.GoodsResp])
def get_my_goods(uid: int, db: Session = Depends(get_db)):
    return db.query(models.Goods).filter(models.Goods.user_id == uid).all()
