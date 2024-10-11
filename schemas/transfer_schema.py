from pydantic import BaseModel
from datetime import date

# Base schema for Transfer
class TransferBase(BaseModel):
    player_id: int
    from_club_id: int
    to_club_id: int
    transfer_date: date
    transfer_fee: float

# Schema for creating a new transfer
class TransferCreate(TransferBase):
    pass

# Schema for returning transfer data
class Transfer(TransferBase):
    transfer_id: int

    class Config:
        orm_mode = True
