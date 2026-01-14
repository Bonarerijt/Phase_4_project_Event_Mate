# EventMate - Event Management App

Full-stack event management application with React + FastAPI.

## 📚 Documentation

- **[TEAM_SETUP.md](TEAM_SETUP.md)** - Installation instructions for team members
- **[TEAM_WORKFLOW.md](TEAM_WORKFLOW.md)** - Branch workflow and task assignments
- **[GIT_INSTRUCTIONS.md](GIT_INSTRUCTIONS.md)** - Git commands and file structure

## Quick Start

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python seed_data.py  # Add sample data
uvicorn app.main:app --reload
```
→ http://localhost:8000  
→ API Docs: http://localhost:8000/docs

### Frontend
```bash
cd frontend
npm install
npm run dev
```
→ http://localhost:5173

## Features
- JWT Authentication
- Create/Join Events
- Leave Reviews
- Custom Black & Grey CSS

## Test in Postman

**Sample Login Credentials:**
- Email: `john@example.com` | Password: `pass123`
- Email: `jane@example.com` | Password: `pass123`
- Email: `mike@example.com` | Password: `pass123`

**Register:**
```
POST http://localhost:8000/auth/register
{"name": "John", "email": "john@test.com", "password": "pass123"}
```

**Login:**
```
POST http://localhost:8000/auth/login
{"email": "john@test.com", "password": "pass123"}
```

**Create Event (use token):**
```
POST http://localhost:8000/events
Authorization: Bearer YOUR_TOKEN
{
  "title": "Tech Meetup",
  "description": "Great event",
  "location": "SF",
  "datetime": "2024-12-31T18:00:00"
}
```

## Structure
```
EventMate/
├── backend/
│   ├── app/
│   │   ├── models/      # User, Event, Participation, Review
│   │   ├── routers/     # API endpoints
│   │   ├── schemas/     # Pydantic models
│   │   ├── utils/       # Auth helpers
│   │   ├── config.py
│   │   ├── database.py
│   │   └── main.py
│   ├── .env
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/  # Navbar, Footer, ProtectedRoute
    │   ├── context/     # AuthContext
    │   ├── pages/       # All pages
    │   ├── services/    # API calls
    │   ├── styles/      # Custom CSS
    │   ├── App.jsx
    │   └── main.jsx
    ├── index.html
    └── package.json
```

## Routes
- `/` - Home
- `/login` - Login
- `/register` - Register
- `/forgot-password` - Reset password
- `/events` - Browse events
- `/events/:id` - Event details (Protected)
- `/dashboard` - Dashboard (Protected)
- `/my-events` - My events (Protected)
- `/profile` - Profile (Protected)

## API Endpoints
- `POST /auth/register` - Register
- `POST /auth/login` - Login
- `GET /auth/me` - Get user (Protected)
- `GET /events` - Get all events
- `POST /events` - Create event (Protected)
- `GET /events/{id}` - Get event
- `PATCH /events/{id}` - Update event (Protected)
- `DELETE /events/{id}` - Delete event (Protected)
- `POST /participation` - Join event (Protected)
- `PATCH /participation/{id}` - Update participation (Protected)
- `POST /reviews` - Create review (Protected)
- `GET /reviews/{event_id}` - Get reviews
- `DELETE /reviews/{id}` - Delete review (Protected)
