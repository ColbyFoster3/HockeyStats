from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db # Database session dependency
from app.schemas.team import TeamCreate, TeamRead # Pydantic models
from app.services.team import create_team, get_teams, get_team_by_id # Business logic

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.post("/", response_model=TeamRead)
def create(team: TeamCreate, db: Session = Depends(get_db)):
    return create_team(db, team)

@router.get("/all", response_model=list[TeamRead])
def list_teams(db: Session = Depends(get_db)):
    return get_teams(db)

@router.get("/{team_id}", response_model=TeamRead)
def list_teams(team_id: int, db: Session = Depends(get_db)):
    team = get_team_by_id(db, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team
