from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import get_db
from pydantic_schemas.user import UserCreate, UserResponse
from api.db_helpers.user import create_user, find_user
from auth import verify_password, create_access_token

router = APIRouter()

@router.post('/api/v1/register_user', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_user(user, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Bad Request. Please try again."
        )

    return user

@router.post('/api/v1/login', status_code=status.HTTP_200_OK)
def login(credentials: UserCreate, db: Session = Depends(get_db)):
    db_user = find_user(credentials, db)

    if not db_user or not verify_password(credentials.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_NOT_FOUND,
            detail="Invalid Credentials, try again."
        )

    token = create_access_token({"sub": db_user.email})

    return {"access_token": token, "token_type": "bearer"}