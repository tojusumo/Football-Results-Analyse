from pydantic import BaseModel
from typing import Optional
from datetime import date

# Base schema for player data
class PlayerBase(BaseModel):
    name: str
    date_of_birth: date
    nationality: str
    position: str
    current_club: Optional[int] = None  # Optional club ID
    contract_start_date: date
    contract_end_date: date

# Schema for creating a new player
class PlayerCreate(PlayerBase):
    pass

# Schema for returning player data
class Player(PlayerBase):
    player_id: int

    class Config:
        orm_mode = True
