from fastapi import HTTPException, Request
from jose import JWTError, jwt

SECRET_KEY = 'user-secret-key-1'
ALGORITM = 'HS256'

def verify_token(request: Request):
    """Extract and verify JWT token from the request headers."""

    token = request.headers.get('Authorization')
    if not token:
        raise HTTPException(status_code=401, detail="Token missing or Invalid")

    try:
        payload = jwt.decode(token.split(" ")[1], SECRET_KEY, algorithms=[ALGORITM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
