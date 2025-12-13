from fastapi import FastAPI
from app.api.users import router as user_router
from app.api.home import router as home_router

app = FastAPI(title="Hockey Stats Project")

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(home_router, tags=["home"])