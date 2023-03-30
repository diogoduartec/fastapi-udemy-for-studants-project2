from typing import List
from fastapi import APIRouter, Depends, Response, status, Query
from sqlalchemy.orm import Session
from app.schemas.category import Category, CategoryOutput
from app.routes.deps import get_db_session, auth
from app.use_cases.category import CategoryUseCases
from fastapi_pagination import Page, add_pagination


router = APIRouter(prefix='/category', tags=['Category'], dependencies=[Depends(auth)])


@router.post('/add', status_code=status.HTTP_201_CREATED, description="Add new category")
def add_category(
    category: Category,
    db_session: Session = Depends(get_db_session)
):
    uc = CategoryUseCases(db_session=db_session)
    uc.add_category(category=category)
    return Response(status_code=status.HTTP_201_CREATED)


@router.get('/list', response_model=Page[CategoryOutput], description="List categories")
def list_categories(
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(50, ge=1, le=100, description="Size of page"),
    db_session: Session = Depends(get_db_session)
):
    uc = CategoryUseCases(db_session=db_session)
    response = uc.list_categories(page=page, size=size)

    return response


@router.delete('/delete/{id}', description="Delete category")
def delete_category(
    id: int,
    db_sesion: Session = Depends(get_db_session)
):
    uc = CategoryUseCases(db_session=db_sesion)
    uc.delete_category(id=id)

    return Response(status_code=status.HTTP_200_OK)
