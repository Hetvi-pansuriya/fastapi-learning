from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
    return {"message": "Hello World"}

@app.get("/expense")
def get_expenses():
    return {"expenses":["food - 500","travel - 1200"]}

