from sqlalchemy import Column, ForeignKey, Integer, String

from db.base import Base


class Match(Base):
    __tablename__ = 'match'
    
    match_id = Column(Integer,primary_key=True,index=True)
    date = Column(String)
    home_club_id = Column(Integer,ForeignKey("team.team_id"))
    away_club_id = Column(Integer,ForeignKey("team.team_id"))
    score = Column(String)
    competition = Column(Integer,ForeignKey("competition.competition_id"))