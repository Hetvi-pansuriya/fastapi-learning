# FastAPI Learning

Learning FastAPI step by step, building REST APIs with Python.

## Structure
- first-api: Expense Tracker API with full CRUD + SQLite database

## Files
- main.py: FastAPI routes and application logic
- database.py: SQLite database connection using SQLAlchemy
- models.py: Database table definitions
- requirements.txt: Python dependencies

## What I Built
A complete REST API for tracking expenses:
- GET / -- Home route
- GET /expenses -- Returns all expenses from database
- POST /expenses -- Adds expense, saves to database permanently
- GET /expenses/{category} -- Filter expenses by category
- DELETE /expenses/{id} -- Delete expense by ID
- PUT /expenses/{id} -- Update expense by ID

## How to run
pip install -r requirements.txt
cd first-api
uvicorn main:app --reload

## Test the API
Open http://127.0.0.1:8000/docs in browser

## What I Learned
- Day 1: FastAPI setup, GET routes, Swagger docs
- Day 2: POST requests, Pydantic models, in-memory storage
- Day 3: Path parameters, DELETE route
- Day 4: PUT route, complete CRUD
- Day 5: Revised all CRUD operations
- Day 6: SQLAlchemy, SQLite database connection setup
- Day 7: Complete database integration, data persistence, gitignore, requirements