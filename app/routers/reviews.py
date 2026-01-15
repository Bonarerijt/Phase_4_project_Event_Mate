from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.review import Review
from ..models.event import Event
from ..models.user import User
from ..schemas.review import ReviewCreate, ReviewResponse
from ..utils.dependencies import get_current_user
