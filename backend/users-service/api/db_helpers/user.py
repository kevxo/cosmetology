import uuid

from fastapi import status, HTTPException
from models.user import User
from sqlalchemy.orm import Session
from pydantic_schemas.user import UserCreate
from auth import hash_password

def create_user(user: UserCreate, db: Session) -> User:
    existing_user = (
        db.query(User).filter(User.email == user.email.lower()).first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )

    created_user = User(
        uuid=str(uuid.uuid4()),
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(created_user)
    db.commit()
    db.refresh(created_user)

    return created_user

def find_user(user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.email == user.email).first()

    return db_user