from fastapi import FastAPI
from app.api.users import router as user_router
from app.api.home import router as home_router
from app.api.players import router as players_router
from app.api.teams import router as teams_router
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

app = FastAPI(title="Hockey Stats Project")

app.include_router(user_router)
app.include_router(home_router)
app.include_router(players_router)
app.include_router(teams_router)