import re
from pydantic import validator
from app.schemas.base import CustomBaseModel


class Product(CustomBaseModel):
    name: str
    slug: str
    price: float
    stock: int

    @validator('slug')
    def validate_slug(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
            raise ValueError('Invalid slug')
        return value
    

    @validator('price')
    def validate_price(cls, value):
        if value <= 0:
            raise ValueError('Invalid price')
        return value
