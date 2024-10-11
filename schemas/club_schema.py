from pydantic import BaseModel
from typing import Optional
from datetime import date

# Base schema for player data
class ClubBase(BaseModel):
    name: str
    founded: Optional[str] = None
    city: str
    stadium: Optional[str] = None  # Optional club ID
    country: str

# Schema for creating a new player
class ClubCreate(ClubBase):
    pass

# Schema for returning player data
class Club(ClubBase):
    club_id: int

    class Config:
        orm_mode = True
