# Sport App

## Description
Backend API for a fitness tracking application.

Users can:
- create an account
- authenticate with JWT
- access protected routes

The goal of the application is to allow users to track their workouts, monitor their progress, and visualize their performance through a dashboard.

---

## Features
- User registration
- User login with JWT authentication
- Protected route to get current user (`/users/me`)

---

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT (python-jose)
- Passlib (bcrypt)

## Project Structure
backend/
├── app/
│ ├── core/ # config, security, dependencies
│ ├── db/ # database setup
│ ├── models/ # SQLAlchemy models
│ ├── schemas/ # Pydantic schemas
│ ├── services/ # business logic
│ ├── routers/ # API routes
│ └── main.py
├── .env.example
└── requirements.txt

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/guillaumelefou/sport-app.git
cd sport-app/backend
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv/Scripts/activate #Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a .env file
```bash
cp .env.example .env
```

### 5. Run the server
```bash
uvicorn app.main:app --reload
```

---

## Usage

### API Documentation
Available at:
http://localhost:8000/docs

### Authentication
1. Use `/auth/login` to get a token
2. Click "Authorize" in Swagger
3. Enter:
Bearer YOUR_TOKEN

### Endpoints

#### Auth
- POST /auth/register
- POST /auth/login

#### Users
- GET /users/me (protected)

---

## Future Improvements
- Routine management (CRUD)
- Workout sessions tracking
- Dashboard with statistics

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Future Improvements
- Routine management (CRUD)
- Workout sessions tracking
- Dashboard with statistics