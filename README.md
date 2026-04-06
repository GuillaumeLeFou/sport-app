# Sport App

## Description
Sport App is a full-stack fitness tracking application.

The goal of the project is to allow users to:
- create an account
- authenticate securely with JWT
- access protected routes
- track their workouts and progress
- visualize their data through a dashboard

This project currently includes a working backend API and the beginning of a frontend interface.

---

## Features

### Backend
- User registration
- User login with JWT authentication
- Protected route to get the current user (`/users/me`)

### Frontend
- Login page
- Connection to backend authentication API

---

## Tech Stack

### Backend
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT (`python-jose`)
- Passlib (`bcrypt`)

### Frontend
- React
- TypeScript
- Vite
- Axios
- React Router

---

## Project Structure

```
├── 📁 backend
│   ├── 📁 app
│   │   ├── 📁 core
│   │   │   ├── 🐍 config.py
│   │   │   ├── 🐍 dependencies.py
│   │   │   └── 🐍 security.py
│   │   ├── 📁 db
│   │   │   ├── 🐍 base.py
│   │   │   └── 🐍 session.py
│   │   ├── 📁 models
│   │   │   └── 🐍 user.py
│   │   ├── 📁 routers
│   │   │   ├── 🐍 auth.py
│   │   │   └── 🐍 users.py
│   │   ├── 📁 schemas
│   │   │   └── 🐍 user.py
│   │   ├── 📁 services
│   │   │   └── 🐍 auth_service.py
│   │   └── 🐍 main.py
│   └── 📄 requirements.txt
├── 📁 frontend
│   ├── 📁 src
│   │   ├── 📁 pages
│   │   │   ├── 📄 Login.tsx
│   │   │   └── 📄 Register.tsx
│   │   ├── 📁 services
│   │   │   └── 📄 api.ts
│   │   ├── 📄 App.tsx
│   │   ├── 🎨 index.css
│   │   └── 📄 main.tsx
│   ├── ⚙️ .gitignore
│   ├── 📝 README.md
│   ├── 📄 eslint.config.js
│   ├── 🌐 index.html
│   ├── ⚙️ package-lock.json
│   ├── ⚙️ package.json
│   ├── ⚙️ tsconfig.app.json
│   ├── ⚙️ tsconfig.json
│   ├── ⚙️ tsconfig.node.json
│   └── 📄 vite.config.ts
├── ⚙️ .gitignore
└── 📝 README.md
```

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/guillaumelefou/sport-app.git
cd sport-app/backend
```

## Backend Setup

### 1. Go to the backend folder
```bash
cd backend
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

### 5. Run the backend server
```bash
uvicorn app.main:app --reload
```

backend available at: http://127.0.0.1:8000

Swagger documentation: http://127.0.0.1:8000/docs

---

## Frontend Setup

### 1. Open a new terminal go to the frontend folder
```bash
cd frontend
```

### 2. Install dependencies
```bash
npm install
```

### 3. Run the frontend server
```bash
npm run dev
```

frontend available at: http://localhost:5173

---

## Authentication
To authenticate:
1. Register a user with POST /auth/register
2. Login with POST /auth/login
3. Use the returned token for protected routes

In Swagger:
1. Click on "Authorize"
2. Login through /auth/login
3. Use the token to access endpoints like /users/me

---

## API Endpoints

### Auth
- POST /auth/register
- POST /auth/login

### Users
- GET /users/me (protected)

---

## Future Improvements
- Do the register page
- Exercise management (CRUD)
- Routine management (CRUD)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Guillaume Vanvilthoven  
Junior Fullstack Developer  