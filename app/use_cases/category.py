from sqlalchemy.orm import Session
from app.db.models import Category as CategoryModel
from app.schemas.category import Category, CategoryOutput



class CategoryUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def add_category(self, category: Category):
        category_model = CategoryModel(**category.dict())
        self.db_session.add(category_model)
        self.db_session.commit()

    def list_categories(self):
        categories_on_db = self.db_session.query(CategoryModel).all()
        categories_output = [
            self.serialize_category(category_model)
            for category_model in categories_on_db
        ]
        return categories_output

    def serialize_category(self, category_model: CategoryModel):
        return CategoryOutput(**category_model.__dict__)
