from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.models.user import User
from app.services.s3 import upload_avatar
from app.services.dynamodb import (
    save_user,
    get_users as load_users
)

router = APIRouter()


@router.get("/users")
def get_users():
    return load_users()


@router.post("/user")
async def create_user(
    name: str = Form(...),
    email: str = Form(...),
    avatar: UploadFile = File(...)
):

    if not avatar.filename:
        raise HTTPException(
            status_code=400,
            detail="Avatar file is required"
        )

    try:

        avatar_url = upload_avatar(avatar)

        user = User(
            name=name,
            email=email,
            avatar_url=avatar_url
        )

        save_user(user.model_dump())

        return user

    except Exception as exc:

        raise HTTPException(
            status_code=503,
            detail=str(exc)
        )