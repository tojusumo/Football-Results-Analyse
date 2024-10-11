from sqlalchemy import Column, Integer, String
from db.base import Base


class Competition(Base):
    __tablename__ = "competition"
    
    
    competition_id = Column(Integer,primary_key=True,index=True)
    competition_name = Column(String)
    season = Column(String)
    country = Column(String)