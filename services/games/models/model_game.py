from pydantic import BaseModel

class Game(BaseModel):
    category_uuids: list[str]
    price: int
    title: str
    uuid: str

class GamesModel(BaseModel):
    games: list[Game]
    meta: dict