from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
from app.db.models import Product as ProductModel
from app.db.models import Category as CategoryModel
from app.schemas.product import Product

class ProductUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_product(self, product: Product, category_slug: str):
        category = self.db_session.query(CategoryModel).filter_by(slug=category_slug).first()
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No category was found with slug {category_slug}')
        
        product_model = ProductModel(**product.dict())
        product_model.category_id = category.id

        self.db_session.add(product_model)
        self.db_session.commit()

    def update_product(self, id: int, product: Product):
        product_on_db = self.db_session.query(ProductModel).filter_by(id=id).first()

        if product_on_db is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No product was found with the given id')
        
        product_on_db.name = product.name
        product_on_db.slug = product.slug
        product_on_db.price = product.price
        product_on_db.stock = product.stock

        self.db_session.add(product_on_db)
        self.db_session.commit()
