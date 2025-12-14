from pydantic import BaseModel

# This details what data the Team model will accept when calling the POST endpoint
class TeamBase(BaseModel):
    name: str
    city: str
    abbreviation: str

class TeamCreate(TeamBase):
    pass

class TeamRead(TeamBase):
    id: int

    model_config = {
        "from_attributes": True
    }
