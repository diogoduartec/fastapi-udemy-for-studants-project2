import pytest
from app.db.connection import Session
from app.db.models import Category as CategoryModels


@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()


@pytest.fixture()
def categories_on_db(db_session):
    categories = [
        CategoryModels(name='Roupa', slug='roupa'),
        CategoryModels(name='Carro', slug='carro'),
        CategoryModels(name='Itens de cozinha', slug='itens-de-cozinha'),
        CategoryModels(name='Decoracao', slug='decoracao'),
    ]

    for category in categories:
        db_session.add(category)
    db_session.commit()

    for category in categories:
        db_session.refresh(category)
    
    yield categories

    for category in categories:
        db_session.delete(category)
    db_session.commit()
