from fastapi import status, Response, Depends, APIRouter
from sqlalchemy.orm import Session
from app.routes.deps import get_db_session
from app.schemas.user import User
from app.use_cases.user import UserUseCases


router = APIRouter(prefix='/user')

@router.post('/register')
def user_register(
    user: User,
    db_session: Session = Depends(get_db_session)
):
    uc = UserUseCases(db_session=db_session)
    uc.register_user(user=user)
    return Response(status_code=status.HTTP_201_CREATED)
