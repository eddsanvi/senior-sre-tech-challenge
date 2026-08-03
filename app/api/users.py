from fastapi import APIRouter
from app.models.user import User

router = APIRouter()

users = []


@router.get("/users")
def get_users():
    return users