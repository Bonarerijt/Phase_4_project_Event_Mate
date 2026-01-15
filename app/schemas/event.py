from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventBase(BaseModel):
    title: str
    description: str
    location: str
    datetime: datetime
    organizer_id: int