from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    name: str
    email: str

class UserSchema(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True  # was orm_mode=True
