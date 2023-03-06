import pytest
from app.schemas.user import User


def test_user_schema():
    user = User(username='Diogo', password='pass#')
    assert user.dict() == {
        'username': 'Diogo',
        'password': 'pass#'
    }

def test_user_schema_invalid_username():
    with pytest.raises(ValueError):
        user = User(username='João#', password='pass#')
