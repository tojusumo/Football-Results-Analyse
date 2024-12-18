from sqlalchemy import Column,ForeignKey,Integer,String
from db.base import Base



class Player(Base):
    __tablename__ = "player"
    
    
    player_id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    date_of_birth = Column(String)
    position = Column(String)
    nationality = Column(String)
    current_club = Column(Integer,ForeignKey("club.club_id"))
    contract_start_date = Column(String)
    contract_end_date = Column(String)
    
    
