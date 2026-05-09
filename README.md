# FastAPI Learning

Learning FastAPI step by step, building REST APIs with Python.

## Structure
- first-api: Expense Tracker API with GET and POST routes

## What I Built
A REST API for tracking expenses with:
- GET / — Home route
- GET /expenses — Returns all expenses
- POST /expenses — Adds a new expense with validation

## How to run
- pip install fastapi uvicorn
- cd first-api
- uvicorn main:app --reload

## Test the API
Open http://127.0.0.1:8000/docs in browser
Use the Swagger UI to test all routes

## What I Learned
Day 1:
- Creating a FastAPI app
- Defining GET routes
- Automatic Swagger docs at /docs
<<<<<<< HEAD

Day 2:
- POST requests
- Pydantic models for data validation
- Storing data in memory using a list
- Testing API with Swagger UI