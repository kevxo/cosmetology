from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import get_db
from pydantic_schemas.user import UserCreate, UserResponse
from api.db_helpers.user import create_user

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