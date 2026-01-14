# Team Member Branch Instructions

## Initial Setup (Everyone Does This First)

```bash
# Clone repository
git clone <repository-url>
cd Phase_4_project_Event_Mate

# Setup backend
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cd ..

# Setup frontend
cd frontend
npm install
cd ..
```

---

## MEMBER 1 - Backend Authentication

### Branch Name: `feature/backend-auth`

### Your Responsibility
Implement user authentication system with JWT tokens.

### Files to Implement
1. `backend/app/models/user.py` - User database model
2. `backend/app/schemas/user.py` - User Pydantic schemas
3. `backend/app/utils/auth.py` - Password hashing & JWT functions
4. `backend/app/utils/dependencies.py` - Get current user dependency
5. `backend/app/routers/auth.py` - Auth endpoints (register, login, me)

### Git Workflow
```bash
# Create and switch to your branch
git checkout -b feature/backend-auth

# Work on your files
# ... implement the files ...

# Test your work
cd backend
source venv/bin/activate
uvicorn app.main:app --reload
# Test at http://localhost:8000/docs

# Commit your changes
git add backend/app/models/user.py
git add backend/app/schemas/user.py
git add backend/app/utils/auth.py
git add backend/app/utils/dependencies.py
git add backend/app/routers/auth.py
git commit -m "Implement backend authentication system"

# Push to remote
git push origin feature/backend-auth

# Create Pull Request on GitHub
```

### What to Implement

**user.py (Model):**
- User table with: id, name, email, password_hash, role, created_at
- Relationships to events, participations, reviews

**user.py (Schema):**
- UserCreate, UserLogin, UserResponse, Token schemas

**auth.py (Utils):**
- verify_password(), get_password_hash(), create_access_token(), decode_token()

**dependencies.py:**
- get_current_user() function using JWT

**auth.py (Router):**
- POST /auth/register
- POST /auth/login
- GET /auth/me

---

## MEMBER 2 - Backend Features

### Branch Name: `feature/backend-features`

### Your Responsibility
Implement events, participation, and reviews functionality.

### Files to Implement
1. `backend/app/models/event.py` - Event model
2. `backend/app/models/participation.py` - Participation model
3. `backend/app/models/review.py` - Review model
4. `backend/app/schemas/event.py` - Event schemas
5. `backend/app/schemas/participation.py` - Participation schemas
6. `backend/app/schemas/review.py` - Review schemas
7. `backend/app/routers/events.py` - Event endpoints
8. `backend/app/routers/participation.py` - Participation endpoints
9. `backend/app/routers/reviews.py` - Review endpoints

### Git Workflow
```bash
# Create and switch to your branch
git checkout -b feature/backend-features

# Work on your files
# ... implement the files ...

# Test your work
cd backend
source venv/bin/activate
uvicorn app.main:app --reload

# Commit your changes
git add backend/app/models/
git add backend/app/schemas/
git add backend/app/routers/
git commit -m "Implement events, participation, and reviews"

# Push to remote
git push origin feature/backend-features

# Create Pull Request on GitHub
```

### What to Implement

**Models:**
- Event: id, title, description, location, datetime, organizer_id
- Participation: id, user_id, event_id, status
- Review: id, event_id, user_id, rating, comment

**Routers:**
- Events: GET, POST, GET/:id, PATCH/:id, DELETE/:id
- Participation: POST, PATCH/:id
- Reviews: POST, GET/:event_id, DELETE/:id

---

## MEMBER 3 - Backend Setup & Database

### Branch Name: `feature/backend-setup`

### Your Responsibility
Setup FastAPI app, database connection, and seed data.

### Files to Implement
1. `backend/app/config.py` - Environment configuration
2. `backend/app/database.py` - Database connection
3. `backend/app/main.py` - FastAPI app setup
4. `backend/seed_data.py` - Sample data script

### Git Workflow
```bash
# Create and switch to your branch
git checkout -b feature/backend-setup

# Work on your files
# ... implement the files ...

# Test your work
cd backend
source venv/bin/activate
python seed_data.py
uvicorn app.main:app --reload

# Commit your changes
git add backend/app/config.py
git add backend/app/database.py
git add backend/app/main.py
git add backend/seed_data.py
git commit -m "Setup FastAPI app and database"

# Push to remote
git push origin feature/backend-setup

# Create Pull Request on GitHub
```

### What to Implement

**config.py:**
- Settings class with DATABASE_URL, SECRET_KEY, ALGORITHM

**database.py:**
- SQLAlchemy engine, SessionLocal, Base, get_db()

**main.py:**
- FastAPI app with CORS, router includes, root endpoint

**seed_data.py:**
- Create 3 users, 5 events, participations, reviews

---

## MEMBER 4 - Frontend Auth & Routing

### Branch Name: `feature/frontend-auth`

### Your Responsibility
Setup React app, authentication context, and routing.

### Files to Implement
1. `frontend/src/context/AuthContext.jsx` - Auth state management
2. `frontend/src/services/api.js` - API calls with axios
3. `frontend/src/components/common/ProtectedRoute.jsx` - Route guard
4. `frontend/src/components/common/Navbar.jsx` - Navigation bar
5. `frontend/src/components/common/Footer.jsx` - Footer
6. `frontend/src/App.jsx` - Main app with routes
7. `frontend/src/main.jsx` - Entry point

### Git Workflow
```bash
# Create and switch to your branch
git checkout -b feature/frontend-auth

# Work on your files
# ... implement the files ...

# Test your work
cd frontend
npm run dev
# Open http://localhost:5173

# Commit your changes
git add frontend/src/context/
git add frontend/src/services/
git add frontend/src/components/
git add frontend/src/App.jsx
git add frontend/src/main.jsx
git commit -m "Setup React routing and authentication"

# Push to remote
git push origin feature/frontend-auth

# Create Pull Request on GitHub
```

### What to Implement

**AuthContext.jsx:**
- user state, login(), register(), logout()
- Token storage in localStorage

**api.js:**
- axios instance with interceptors
- authAPI, eventsAPI, participationAPI, reviewsAPI

**App.jsx:**
- React Router with 9 routes
- 5 protected routes

---

## MEMBER 5 - Frontend Pages

### Branch Name: `feature/frontend-pages`

### Your Responsibility
Create all page components for the application.

### Files to Implement
1. `frontend/src/pages/Home.jsx` - Landing page
2. `frontend/src/pages/Login.jsx` - Login form
3. `frontend/src/pages/Register.jsx` - Registration form
4. `frontend/src/pages/ForgotPassword.jsx` - Password reset
5. `frontend/src/pages/Events.jsx` - Events list
6. `frontend/src/pages/EventDetail.jsx` - Event details with reviews
7. `frontend/src/pages/Dashboard.jsx` - User dashboard
8. `frontend/src/pages/MyEvents.jsx` - Create/manage events
9. `frontend/src/pages/Profile.jsx` - User profile

### Git Workflow
```bash
# Create and switch to your branch
git checkout -b feature/frontend-pages

# Work on your files
# ... implement the files ...

# Test your work
cd frontend
npm run dev

# Commit your changes
git add frontend/src/pages/
git commit -m "Implement all frontend pages"

# Push to remote
git push origin feature/frontend-pages

# Create Pull Request on GitHub
```

### What to Implement

**Each Page Should:**
- Use AuthContext for user state
- Call API using services/api.js
- Handle loading and error states
- Use React Router for navigation

**Key Features:**
- Login/Register: Form validation
- Events: Display all events
- EventDetail: Join event, leave reviews
- MyEvents: Create event form
- Dashboard: Quick links

---

## MEMBER 6 - Frontend Styling

### Branch Name: `feature/frontend-styling`

### Your Responsibility
Create custom CSS with black and grey theme.

### Files to Implement
1. `frontend/src/styles/App.css` - Component styles
2. `frontend/src/index.css` - Global styles

### Git Workflow
```bash
# Create and switch to your branch
git checkout -b feature/frontend-styling

# Work on your files
# ... implement the files ...

# Test your work
cd frontend
npm run dev

# Commit your changes
git add frontend/src/styles/
git add frontend/src/index.css
git commit -m "Add custom black and grey CSS theme"

# Push to remote
git push origin feature/frontend-styling

# Create Pull Request on GitHub
```

### What to Implement

**Color Scheme:**
- Background: #1a1a1a (dark black)
- Cards: #2a2a2a (grey)
- Navbar: #000 (pure black)
- Text: #e0e0e0 (light grey)
- Buttons: #333, #666

**Styles for:**
- Navbar, Footer
- Forms (inputs, buttons)
- Cards (events, reviews)
- Grid layouts
- Responsive design

---

## Merging Workflow (Team Lead)

### Order of Merging
1. Merge `feature/backend-setup` first (database & config)
2. Merge `feature/backend-auth` (authentication)
3. Merge `feature/backend-features` (events, reviews)
4. Merge `feature/frontend-auth` (routing & context)
5. Merge `feature/frontend-pages` (all pages)
6. Merge `feature/frontend-styling` (CSS)

### Merge Commands
```bash
# Switch to main branch
git checkout main

# Pull latest changes
git pull origin main

# Merge feature branch
git merge feature/backend-setup

# Push to remote
git push origin main

# Repeat for each branch in order
```

---

## Conflict Resolution

If you get merge conflicts:

```bash
# Pull latest main
git checkout main
git pull origin main

# Switch back to your branch
git checkout feature/your-branch

# Merge main into your branch
git merge main

# Fix conflicts in files
# ... edit conflicting files ...

# Add resolved files
git add .

# Commit merge
git commit -m "Resolve merge conflicts"

# Push updated branch
git push origin feature/your-branch
```

---

## Testing Checklist

### Backend Testing
- [ ] Server starts without errors
- [ ] All endpoints visible at /docs
- [ ] Can register new user
- [ ] Can login and get token
- [ ] Protected endpoints require token
- [ ] Can create/read/update/delete events
- [ ] Can join events
- [ ] Can leave reviews

### Frontend Testing
- [ ] App loads without errors
- [ ] Can navigate between pages
- [ ] Can register new account
- [ ] Can login with credentials
- [ ] Protected routes redirect to login
- [ ] Can view all events
- [ ] Can create new event
- [ ] Can join events
- [ ] Can leave reviews
- [ ] Styling looks good (black/grey theme)

---

## Communication

### Daily Standup (Suggested)
- What did you complete yesterday?
- What will you work on today?
- Any blockers?

### Before Creating PR
- Test your code locally
- Make sure backend/frontend runs
- Write clear commit messages
- Add description to PR

### Code Review
- Review each other's PRs
- Test the changes locally
- Provide constructive feedback
- Approve when ready

---

## Quick Reference

**Start Backend:**
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload
```

**Start Frontend:**
```bash
cd frontend
npm run dev
```

**Create Branch:**
```bash
git checkout -b feature/your-feature
```

**Push Branch:**
```bash
git add .
git commit -m "Your message"
git push origin feature/your-feature
```

**Update from Main:**
```bash
git checkout main
git pull origin main
git checkout feature/your-branch
git merge main
```
