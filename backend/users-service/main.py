from fastapi import FastAPI

from database import engine
from api.routes import api_router
from models.base import Base

def create_tables():
    Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_router)

def start_services():
    app = FastAPI(title="Users Service", version="1.0.0")
    create_tables()
    include_router(app)

    return app

app = start_services()

@app.get('/')
def user_service():
    return {"message": "Users Service is running"}
