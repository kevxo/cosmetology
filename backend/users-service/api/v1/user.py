from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/users')
def get_all_users():
    return {"msg": "Hello World!"}