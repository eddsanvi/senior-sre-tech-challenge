from fastapi import APIRouter, UploadFile, File, Form
from app.models.user import User

router = APIRouter()

users = []


@router.get("/users")
def get_users():
    return users


@router.post("/user")
async def create_user(
    name: str = Form(...),
    email: str = Form(...),
    avatar: UploadFile = File(...)
):

    new_user = {
        "name": name,
        "email": email,
        "avatar_url": f"/avatars/{avatar.filename}"
    }

    users.append(new_user)

    return new_user