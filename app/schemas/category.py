import re
from pydantic import validator
from app.schemas.base import CustomBaseModel


class Category(CustomBaseModel):
    name: str
    slug: str

    @validator('slug')
    def validate_slug(cls, value):
        if not re.match('^([a-z]|[0-9]|-|_)+$', value):
            raise ValueError('Invalid slug')
        return value


class CategoryOutput(Category):
    id: int

    class Config:
        orm_mode=True
