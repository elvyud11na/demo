from typing import List
from pydantic import BaseModel

class Game(BaseModel):
    category_uuids: List[str]
    price: int
    title: str
    uuid: str

class GamesByCategoryModel(BaseModel):
    games: List[Game]
    meta: dict