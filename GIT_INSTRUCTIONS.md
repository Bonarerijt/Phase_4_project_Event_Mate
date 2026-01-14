# Git Commit Instructions

## Files to Commit (Empty Structure)

### Root Files
- `.gitignore`
- `README.md`
- `TEAM_SETUP.md`

### Backend Files
```
backend/
├── app/
│   ├── models/
│   │   ├── __init__.py (empty)
│   │   ├── event.py (empty)
│   │   ├── participation.py (empty)
│   │   ├── review.py (empty)
│   │   └── user.py (empty)
│   ├── routers/
│   │   ├── __init__.py (empty)
│   │   ├── auth.py (empty)
│   │   ├── events.py (empty)
│   │   ├── participation.py (empty)
│   │   └── reviews.py (empty)
│   ├── schemas/
│   │   ├── __init__.py (empty)
│   │   ├── event.py (empty)
│   │   ├── participation.py (empty)
│   │   ├── review.py (empty)
│   │   └── user.py (empty)
│   ├── utils/
│   │   ├── __init__.py (empty)
│   │   ├── auth.py (empty)
│   │   └── dependencies.py (empty)
│   ├── __init__.py (empty)
│   ├── config.py (empty)
│   ├── database.py (empty)
│   └── main.py (empty)
├── .env (keep this file with content)
├── requirements.txt (keep this file with content)
└── seed_data.py (empty)
```

### Frontend Files
```
frontend/
├── src/
│   ├── components/common/
│   │   ├── Footer.jsx (empty)
│   │   ├── Navbar.jsx (empty)
│   │   └── ProtectedRoute.jsx (empty)
│   ├── context/
│   │   └── AuthContext.jsx (empty)
│   ├── pages/
│   │   ├── Dashboard.jsx (empty)
│   │   ├── EventDetail.jsx (empty)
│   │   ├── Events.jsx (empty)
│   │   ├── ForgotPassword.jsx (empty)
│   │   ├── Home.jsx (empty)
│   │   ├── Login.jsx (empty)
│   │   ├── MyEvents.jsx (empty)
│   │   ├── Profile.jsx (empty)
│   │   └── Register.jsx (empty)
│   ├── services/
│   │   └── api.js (empty)
│   ├── styles/
│   │   └── App.css (empty)
│   ├── App.jsx (empty)
│   ├── index.css (empty)
│   └── main.jsx (empty)
├── index.html (minimal HTML)
├── package.json (keep this file with content)
└── vite.config.js (keep this file with content)
```

---

## Files NOT to Commit (Ignored by .gitignore)

- `backend/venv/` - Virtual environment
- `backend/__pycache__/` - Python cache
- `backend/eventmate.db` - Database file
- `frontend/node_modules/` - Node dependencies
- `frontend/package-lock.json` - Lock file (optional)

---

## Git Commands

```bash
# Initialize git (if not already)
cd /home/mungai/Documents/P-Projects/Phase_4_project_Event_Mate
git init

# Add remote repository
git remote add origin <your-repo-url>

# Add all files
git add .

# Check what will be committed
git status

# Commit
git commit -m "Initial project structure - empty files"

# Push to repository
git push -u origin main
```

---

## What Your Team Will Do

1. **Clone the repo:**
   ```bash
   git clone <repo-url>
   cd Phase_4_project_Event_Mate
   ```

2. **Follow TEAM_SETUP.md** to install dependencies

3. **Start implementing** the empty files according to project requirements

4. **Each member works on different files** to avoid conflicts

---

## File Assignment Suggestion

**Member 1 - Backend Auth:**
- `backend/app/models/user.py`
- `backend/app/routers/auth.py`
- `backend/app/schemas/user.py`
- `backend/app/utils/auth.py`
- `backend/app/utils/dependencies.py`

**Member 2 - Backend Features:**
- `backend/app/models/event.py`
- `backend/app/models/participation.py`
- `backend/app/models/review.py`
- `backend/app/routers/events.py`
- `backend/app/routers/participation.py`
- `backend/app/routers/reviews.py`
- `backend/app/schemas/event.py`
- `backend/app/schemas/participation.py`
- `backend/app/schemas/review.py`

**Member 3 - Backend Setup:**
- `backend/app/config.py`
- `backend/app/database.py`
- `backend/app/main.py`
- `backend/seed_data.py`

**Member 4 - Frontend Auth & Routing:**
- `frontend/src/context/AuthContext.jsx`
- `frontend/src/components/common/ProtectedRoute.jsx`
- `frontend/src/components/common/Navbar.jsx`
- `frontend/src/components/common/Footer.jsx`
- `frontend/src/services/api.js`
- `frontend/src/App.jsx`
- `frontend/src/main.jsx`

**Member 5 - Frontend Pages:**
- `frontend/src/pages/Home.jsx`
- `frontend/src/pages/Login.jsx`
- `frontend/src/pages/Register.jsx`
- `frontend/src/pages/ForgotPassword.jsx`
- `frontend/src/pages/Events.jsx`
- `frontend/src/pages/EventDetail.jsx`
- `frontend/src/pages/Dashboard.jsx`
- `frontend/src/pages/MyEvents.jsx`
- `frontend/src/pages/Profile.jsx`

**Member 6 - Frontend Styling:**
- `frontend/src/styles/App.css`
- `frontend/src/index.css`
