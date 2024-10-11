from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel
from typing import List,Optional
from models import Player
from db.base import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
Player.Base.metadata.create_all(bind=engine)

class PlayerBase(BaseModel):
    name: str
    date_of_birth: str
    position: str
    nationality: str
    current_club: int  # Club ID
    contract_start_date: str
    contract_end_date: str

    class Config:
        orm_mode = True  # This tells Pydantic to interact with ORM models

class ClubBase(BaseModel):
    club_name: str
    founded: Optional[str] = None
    stadium: Optional[str] = None
    city: str
    country: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        


@app.post("/club/", response_model=ClubBase)
async def add_club(club: ClubBase, db: Session = Depends(get_db)):
    db_club = player.Club(
        club_name=club.club_name,
        founded=club.founded,
        stadium=club.stadium,
        city=club.city,
        country=club.country
    )
    db.add(db_club)
    db.commit()
    db.refresh(db_club)
    return db_club