import sys
from datetime import datetime, timedelta
from app.database import SessionLocal, engine, Base
from app.models.user import User
from app.models.event import Event
from app.models.participation import Participation
from app.models.review import Review
from app.utils.auth import get_password_hash

def create_sample_data():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        if db.query(User).first():
            print("Database already has data. Skipping...")
            return
        
        users = [
            User(
                name="John Doe",
                email="john@example.com",
                password_hash=get_password_hash("pass123"),
                role="user"
            ),
            User(
                name="Jane Smith",
                email="jane@example.com",
                password_hash=get_password_hash("pass123"),
                role="user"
            ),
            User(
                name="Mike Johnson",
                email="mike@example.com",
                password_hash=get_password_hash("pass123"),
                role="user"
            )
        ]
        
        for user in users:
            db.add(user)
        db.commit()
        print("Created 3 users")