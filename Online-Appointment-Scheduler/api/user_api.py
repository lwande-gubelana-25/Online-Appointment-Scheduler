from fastapi import APIRouter, HTTPException
from src.user import User
from services import user_service

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.post("/")
def create(user: User):
    user_service.create_user(user)
    return user

@router.get("/{user_id}")
def get(user_id: str):
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/")
def list_users():
    return user_service.get_all_users()

@router.delete("/{user_id}")
def delete(user_id: str):
    user_service.delete_user(user_id)
    return {"deleted": user_id}
