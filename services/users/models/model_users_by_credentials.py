from pydantic import BaseModel, UUID4

class UserCredentialsModel(BaseModel):
    email: str
    name: str
    nickname: str
    avatar_url: str
    uuid: UUID4
