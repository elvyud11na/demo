from pydantic import BaseModel
from uuid import UUID

class Categories(BaseModel):

    name: str
    uuid: UUID

class AllCategoriesModel(BaseModel):

    categories: list[Categories]
    meta: dict

