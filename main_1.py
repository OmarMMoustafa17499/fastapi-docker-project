import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal
from cache import get_cache, set_cache

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/", response_model=schemas.UserSchema)
def create_user(user: schemas.UserCreateSchema, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    cache_key = f"user:{db_user.id}"
    set_cache(cache_key, schemas.UserSchema.from_orm(db_user).dict())
    return db_user

@app.get("/user/{user_id}", response_model=schemas.UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    cache_key = f"user:{user_id}"
    cached_user = get_cache(cache_key)
    if cached_user:
        return cached_user
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    set_cache(cache_key, schemas.UserSchema.from_orm(user).dict())
    return user


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
