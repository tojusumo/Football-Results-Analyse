from sqlalchemy.orm import Session
from schemas.player_schema import PlayerCreate
from models import Player

def create_player(db: Session, player: PlayerCreate):
    db_player = Player(
        name=player.name,
        date_of_birth=player.date_of_birth,
        nationality=player.nationality,
        position=player.position,
        current_club=player.current_club,
        contract_start_date=player.contract_start_date,
        contract_end_date=player.contract_end_date
    )
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_player(db: Session, player_id: int):
    return db.query(Player).filter(Player.player_id == player_id).first()

def get_players(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Player).offset(skip).limit(limit).all()

def update_player(db: Session, player_id: int, player: PlayerCreate):
    db_player = get_player(db, player_id)
    if db_player:
        db_player.name = player.name
        db_player.date_of_birth = player.date_of_birth
        db_player.nationality = player.nationality
        db_player.position = player.position
        db_player.current_club = player.current_club
        db_player.contract_start_date = player.contract_start_date
        db_player.contract_end_date = player.contract_end_date
        db.commit()
        db.refresh(db_player)
        return db_player
    return None

def delete_player(db: Session, player_id: int):
    db_player = get_player(db, player_id)
    if db_player:
        db.delete(db_player)
        db.commit()
        return db_player
    return None
