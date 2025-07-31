from fastapi import APIRouter
from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime

router = APIRouter(prefix="/users", tags=["Users"])

# Dummy user model and DB
class User(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime

user_db = []

@router.post("/", response_model=User)
def create_user(name: str, email: str):
    new_user = User(id=str(uuid4()), name=name, email=email, created_at=datetime.utcnow())
    user_db.append(new_user)
    return new_user

@router.get("/", response_model=list[User])
def list_users():
    return user_db
