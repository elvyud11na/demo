from pydantic import BaseModel, UUID4

class Meta(BaseModel):
    total: int

class User(BaseModel):
    avatar_url: str
    email: str
    name: str
    nickname: str
    uuid: UUID4

class UserListModel(BaseModel):
    meta: Meta
    users: list[User]