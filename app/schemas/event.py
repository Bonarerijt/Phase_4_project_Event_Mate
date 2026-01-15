from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventBase(BaseModel):
    title: str
    description: str
    location: str
    datetime: datetime
    organizer_id: int


class EventCreate(EventBase):
    pass
class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    datetime: Optional[datetime] = None
class EventInDB(EventBase):
    id: int

    class Config:
        orm_mode = True