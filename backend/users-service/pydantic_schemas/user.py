from pydantic import BaseModel, EmailStr, Field, field_validator
import re

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=16)

    @field_validator("password")
    def validate_password(cls, value):
        pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
        if not re.match(pattern, value):
            raise ValueError(
                "Password must be at least 8 characters long, contain at least one letter, "
                "one number, and one special character (@$!%*?&)"
            )

        return value


class UserResponse(BaseModel):
    uuid: str
    email: str

    class Config:
        from_attributes = True