import pytest
from app.schemas.category import Category


def test_category_schema():
    category = Category(
        name='Roupa',
        slug='roupa'
    )

    assert category.dict() == {
        'name': 'Roupa',
        'slug': 'roupa'
    }


def test_category_schema_invalid_slug():
    with pytest.raises(ValueError):
        category = Category(
            name='Roupa',
            slug='roupa de cama'
        )

    with pytest.raises(ValueError):
        category = Category(
            name='Roupa',
            slug='cão'
        )
    
    with pytest.raises(ValueError):
        category = Category(
            name='Roupa',
            slug='Roupa'
        )
