from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    avatar_url: str