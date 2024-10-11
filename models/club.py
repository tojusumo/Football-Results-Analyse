from sqlalchemy import Column, Integer, String
from db.base import Base


class Club(Base):
    __tablename__ = "club"
    
    
    club_id = Column(Integer,primary_key=True,index=True)
    club_name = Column(String)
    founded = Column(String)
    stadium = Column(String)
    city = Column(String)
    country = Column(String)