import pytest
from passlib.context import CryptContext
from app.db.connection import Session
from app.db.models import Category as CategoryModel
from app.db.models import Product as ProductModel
from app.db.models import User as UserModel


crypt_context = CryptContext(schemes=['sha256_crypt'])


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
        CategoryModel(name='Roupa', slug='roupa'),
        CategoryModel(name='Carro', slug='carro'),
        CategoryModel(name='Itens de cozinha', slug='itens-de-cozinha'),
        CategoryModel(name='Decoracao', slug='decoracao'),
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


@pytest.fixture()
def product_on_db(db_session):
    category = CategoryModel(name='Carro', slug='carro')
    db_session.add(category)
    db_session.commit()

    product = ProductModel(
        name='Camisa Abibas',
        slug='camisa-abibas',
        price=100.99,
        stock=20,
        category_id=category.id
    )

    db_session.add(product)
    db_session.commit()

    yield product

    db_session.delete(product)
    db_session.delete(category)
    db_session.commit()


@pytest.fixture()
def products_on_db(db_session):
    category = CategoryModel(name='Roupa', slug='roupa')
    db_session.add(category)
    db_session.commit()
    db_session.refresh(category)

    products = [
        ProductModel(name='Camisa Mike', slug='camisa-mike', price=100, stock=10, category_id=category.id),
        ProductModel(name='Moletom Mike', slug='moletom', price=100, stock=10, category_id=category.id),
        ProductModel(name='Camiseta', slug='camiseta-mike', price=100, stock=10, category_id=category.id),
        ProductModel(name='Short', slug='short', price=100, stock=10, category_id=category.id),
    ]

    for product in products:
        db_session.add(product)
    db_session.commit()

    for product in products:
        db_session.refresh(product)
    
    yield products

    for product in products:
        db_session.delete(product)

    db_session.delete(category)
    db_session.commit()


@pytest.fixture()
def user_on_db(db_session):
    user = UserModel(
        username='Carlos',
        password=crypt_context.hash('pass#')
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    
    yield user

    db_session.delete(user)
    db_session.commit()
