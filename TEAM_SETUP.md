# EventMate - Team Setup Guide

## Prerequisites

### Required Software
1. **Python 3.8+**
   ```bash
   python3 --version
   ```

2. **Node.js 16+ and npm**
   ```bash
   node --version
   npm --version
   ```

3. **Git**
   ```bash
   git --version
   ```

---

## Setup Instructions

### 1. Clone Repository
```bash
git clone <repository-url>
cd Phase_4_project_Event_Mate
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create sample data
python seed_data.py

# Start backend server
uvicorn app.main:app --reload
```

**Backend runs at:** http://localhost:8000  
**API Docs:** http://localhost:8000/docs

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# If npm install fails due to network, try:
npm install --registry=https://registry.npmmirror.com

# Start frontend server
npm run dev
```

**Frontend runs at:** http://localhost:5173

---

## Test Credentials

After running `seed_data.py`, use these credentials:

- Email: `john@example.com` | Password: `pass123`
- Email: `jane@example.com` | Password: `pass123`
- Email: `mike@example.com` | Password: `pass123`

---

## Project Structure

```
EventMate/
├── backend/
│   ├── app/
│   │   ├── models/      # Database models
│   │   ├── routers/     # API endpoints
│   │   ├── schemas/     # Pydantic schemas
│   │   ├── utils/       # Auth utilities
│   │   ├── config.py
│   │   ├── database.py
│   │   └── main.py
│   ├── .env
│   ├── requirements.txt
│   └── seed_data.py
└── frontend/
    ├── src/
    │   ├── components/
    │   ├── context/
    │   ├── pages/
    │   ├── services/
    │   ├── styles/
    │   ├── App.jsx
    │   └── main.jsx
    ├── index.html
    └── package.json
```

---

## Common Issues

### Backend Issues

**Issue:** `ModuleNotFoundError: No module named 'fastapi'`  
**Solution:** Activate virtual environment first
```bash
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

**Issue:** `Address already in use`  
**Solution:** Kill existing process
```bash
pkill -f uvicorn
```

### Frontend Issues

**Issue:** `npm install` timeout  
**Solution:** Use alternative registry
```bash
npm install --registry=https://registry.npmmirror.com
```

**Issue:** `vite: not found`  
**Solution:** Install dependencies first
```bash
npm install
```

---

## Development Workflow

1. **Always activate virtual environment** before working on backend
2. **Pull latest changes** before starting work
3. **Run both servers** (backend + frontend) for full testing
4. **Test API** at http://localhost:8000/docs
5. **Test UI** at http://localhost:5173

---

## Git Workflow

```bash
# Pull latest
git pull origin main

# Create feature branch
git checkout -b feature/your-feature

# Make changes and commit
git add .
git commit -m "Description of changes"

# Push to remote
git push origin feature/your-feature

# Create Pull Request on GitHub
```

---

## Quick Start Commands

**Backend:**
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm run dev
```
