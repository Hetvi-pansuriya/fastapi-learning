from fastapi import FastAPI #importing fastapi library
from pydantic import BaseModel #importing BaseModel class from pydantic libraray : it defines what shape data should look like

app = FastAPI() #creating application

expenses=[] #list store expenses in memory, when restart server it resets to empty

class Expense(BaseModel): #shpe of expense
    category: str
    price: float
    date:str

@app.get("/") #decorator- it tells fastapi when someone visit "/" url

def home():
    return {"message": "Hello World"}


@app.get("/expenses") #when someone visit "/expenses" url, returns expenses list
def get_expenses():
    return {"expenses":expenses}

@app.post("/expenses") #accept post request
def add_expenses(expense: Expense): 
    expenses.append(expense.dict()) #convert the Expense object to a dictionary and add it to your list.
    return {"message": "Expense Added", "expense": expense}


