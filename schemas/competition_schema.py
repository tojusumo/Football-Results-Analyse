from pydantic import BaseModel

# Base schema for Competition
class CompetitionBase(BaseModel):
    name: str
    country: str
    season: str

# Schema for creating a new competition
class CompetitionCreate(CompetitionBase):
    pass

# Schema for returning competition data
class Competition(CompetitionBase):
    competition_id: int

    class Config:
        orm_mode = True
