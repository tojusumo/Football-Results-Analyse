from pydantic import BaseModel
from datetime import datetime

# Base schema for Match
class MatchBase(BaseModel):
    home_team_id: int
    away_team_id: int
    competition_id: int
    match_date: datetime
    home_team_score: int = 0  # default score
    away_team_score: int = 0  # default score

# Schema for creating a new match
class MatchCreate(MatchBase):
    pass

# Schema for returning match data
class Match(MatchBase):
    match_id: int

    class Config:
        orm_mode = True
