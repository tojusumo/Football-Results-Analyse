from sqlalchemy import Boolean, Column,ForeignKey,Integer,String
from db.base import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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
    
    
class Club(Base):
    __tablename__ = "club"
    
    
    club_id = Column(Integer,primary_key=True,index=True)
    club_name = Column(String)
    founded = Column(String)
    stadium = Column(String)
    city = Column(String)
    country = Column(String)