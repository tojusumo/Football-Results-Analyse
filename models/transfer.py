from sqlalchemy import Column, Float, ForeignKey, Integer, String

from db.base import Base


class Transfer(Base):
    __tablename__ = 'transfer'
    transfer_id = Column(Integer,primary_key=True,index=True)
    player_id = Column(Integer,ForeignKey("player.player_id"))
    club_out_id = Column(Integer,ForeignKey("team.team_id"))
    club_in_id = Column(Integer,ForeignKey("team.team_id"))
    transfer_date =Column(String)
    fee = Column(Float)