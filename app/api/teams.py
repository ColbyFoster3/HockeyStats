from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession


from app.core.database import get_db, get_db_async # Database session dependency
from app.schemas.team import TeamCreate, TeamRead # Pydantic models
from app.services.team import create_team, get_teams, get_team_by_id # Business logic
from app.services.nhl.team_importer import TeamImporter

router = APIRouter(prefix="/v1/teams", tags=["Teams"])

@router.post("/", response_model=TeamRead)
def create(team: TeamCreate, db: Session = Depends(get_db)):
    return create_team(db, team)

@router.get("/all", response_model=list[TeamRead])
def list_teams(db: Session = Depends(get_db)):
    return get_teams(db)

@router.get("/get/{team_id}", response_model=TeamRead)
def list_teams(team_id: int, db: Session = Depends(get_db)):
    team = get_team_by_id(db, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.get("/import")
async def import_teams(db: AsyncSession = Depends(get_db_async)):
    return await TeamImporter(db).import_teams()