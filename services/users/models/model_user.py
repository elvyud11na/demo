from pydantic import BaseModel, UUID4, field_validator


class UserModel(BaseModel):
    avatar_url: str
    email: str
    name: str
    nickname: str
    uuid: UUID4

    @field_validator("email","name", "nickname", "uuid")# поверяем что в полях не пустота
    def fields_validator(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value  #здесь можно написать просто pass
