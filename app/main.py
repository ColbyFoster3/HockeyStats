from fastapi import FastAPI
from app.api.users import router as user_router
from app.api.home import router as home_router
from app.api.players import router as players_router
from app.api.teams import router as teams_router

app = FastAPI(title="Hockey Stats Project")

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(home_router, tags=["home"])
app.include_router(players_router, tags=["players"])
app.include_router(teams_router)