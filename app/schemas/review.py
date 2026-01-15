from pydantic import BaseModel

class ReviewCreate(BaseModel):
    event_id: int
    rating: int
    comment: str
