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

@app.get("/expenses/{category}") #{category}: path parameter
def get_by_category(category:str): #FastAPI automatically takes the value from the URL and passes it to this function as category
    result=[e for e in expenses if e["category"].lower()==category.lower()] # list comprehension, loop through every expenses of list, check if expense category matches with requested
    return {"expenses":result}

@app.delete("/expenses/{index}") #This defines a DELETE route, {index} is a path parameter
def delete_expense(index:int): #FastAPI takes the number from the URL and passes it to this function as index
    if index < len(expenses): # check if the index is valid
        removed=expenses.pop(index) #pop(index) removes the item at that position from the lis
        return {"message": "Expense Deleted", "expense": removed} 
    return {"message" : "Invalid Index"}