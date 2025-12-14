from sqlalchemy.orm import Session
from app.models.team import Team
from app.schemas.team import TeamCreate

def create_team(db: Session, team: TeamCreate) -> Team:
    db_team = Team(**team.model_dump())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def get_teams(db: Session) -> list[Team]:
    return db.query(Team).all()

def get_team_by_id(db: Session, team_id: int) -> Team | None:
    return db.query(Team).filter(Team.id == team_id).first()