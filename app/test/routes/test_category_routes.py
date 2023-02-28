from fastapi.testclient import TestClient
from fastapi import status
from app.db.models import Category as CategoryModel
from app.main import app

client = TestClient(app)


def test_add_category_route(db_session):
    body = {
        "name": "Roupa",
        "slug": "roupa"
    }
    
    response = client.post('/category/add', json=body)

    assert response.status_code == status.HTTP_201_CREATED
    
    categories_on_db = db_session.query(CategoryModel).all()
    assert len(categories_on_db) == 1
    db_session.delete(categories_on_db[0])
    db_session.commit()


def test_list_categories_route(categories_on_db):
    response = client.get('/category/list')

    assert response.status_code == status.HTTP_200_OK
    data = response.json()

    assert len(data) == 4
    assert data[0] == {
        "name": categories_on_db[0].name,
        "slug": categories_on_db[0].slug,
        "id": categories_on_db[0].id
    }
