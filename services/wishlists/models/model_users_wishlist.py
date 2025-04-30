from pydantic import BaseModel, UUID4

class Item(BaseModel):
    category_uuids: list[UUID4]
    price: int
    title: str
    uuid: UUID4

class UsersWishlistModel(BaseModel):
    items: list[Item]
    user_uuid: UUID4