from pydantic import BaseModel

class GameModel(BaseModel):
    category_uuids: list[str]
    price: int
    title: str
    uuid: str