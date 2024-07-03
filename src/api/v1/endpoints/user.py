from uuid import UUID

from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi import Depends
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from core.deps import get_session
from core.deps import get_current_user
from core.auth import authenticate
from core.auth import create_access_token
from models.user_model import UserModel
from schemas.user_schema import CreateUserSchema
from schemas.user_schema import GetUserSchema
from schemas.user_schema import UpdateUserSchema
from schemas.generic_schema import BaseLoginSchema
from schemas.generic_schema import HttpDetail
from api.v1.data.crud import user_crud as crud
from api.v1.data.template.user_template import UpdateUserBody
from api.v1.data.template.user_template import CreateUserBody


router = APIRouter()


@router.post("/login", status_code=status.HTTP_200_OK, response_model=BaseLoginSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    user = await authenticate(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='User info incorrect')
    
    return JSONResponse({"acess_token": create_access_token(user.user_uuid), "token_type": "bearer"})


@router.get("/logged", status_code=status.HTTP_200_OK, response_model=GetUserSchema)
def get_logged_user(logged_user: UserModel = Depends(get_current_user)):
    return logged_user


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=GetUserSchema)
async def create_user(user: CreateUserSchema = CreateUserBody, db: AsyncSession = Depends(get_session)):
    new_user: UserModel = UserModel(**user.model_dump())
    try:
        response = await crud.create_user_query(new_user, db)
        return response
    
    except IntegrityError:
        raise HTTPException(status.HTTP_409_CONFLICT, 'User with this email already registered')


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[GetUserSchema])
async def get_users(db: AsyncSession = Depends(get_session)):
    return await crud.get_users_query(db)


@router.get("/{user_uuid}", status_code=status.HTTP_200_OK, response_model=GetUserSchema)
async def get_user(user_uuid: UUID, db: AsyncSession = Depends(get_session)):
    response = await crud.get_user_query(user_uuid, db)
    if not response:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'User not found')
    
    return response


@router.patch("/{user_uuid}", status_code=status.HTTP_202_ACCEPTED, response_model=GetUserSchema)
async def update_user(user_uuid: UUID, user: UpdateUserSchema = UpdateUserBody, db: AsyncSession = Depends(get_session)):
    try:
        response = await crud.update_user_query(user_uuid, user, db)
    except IntegrityError:
        raise HTTPException(status.HTTP_409_CONFLICT, 'User email conflict')

    if not response:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'User not found')

    return response


@router.delete("/{user_uuid}", status_code=status.HTTP_200_OK, response_model=HttpDetail)
async def delete_user(user_uuid: UUID, db: AsyncSession = Depends(get_session)):
    check_user = await crud.get_user_query(user_uuid, db)
    if not check_user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'User not found')
    
    await crud.delete_user_query(user_uuid, db)
    
    return HttpDetail(detail= 'User deleted successfully')

