from pydantic import BaseModel

# This details what data the Team model will accept when calling the POST endpoint
class TeamBase(BaseModel):
    name: str
    city: str | None = None
    abbreviation: str | None = None
    api_web_nhle_abr: str | None = None
    api_nhle_id: int | None = None

class TeamCreate(TeamBase):
    pass

class TeamRead(TeamBase):
    id: int

    model_config = {
        "from_attributes": True
    }
