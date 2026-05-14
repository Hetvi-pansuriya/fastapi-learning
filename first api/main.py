from fastapi import FastAPI, Depends #importing fastapi library
from pydantic import BaseModel #importing BaseModel class from pydantic libraray : it defines what shape data should look like
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine) # create table in database

app = FastAPI() #creating application

#pydantic schema for request validation
class ExpenseSchema(BaseModel):
    category:str
    price:float
    date:str

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# expenses=[] #list store expenses in memory, when restart server it resets to empty

@app.get("/") #decorator- it tells fastapi when someone visit "/" url

def home():
    return {"message": "Hello World"}


@app.get("/expenses") #when someone visit "/expenses" url, returns expenses list
def get_expenses(db: Session=Depends(get_db)):
    expenses=db.query(models.Expense).all()
    return {"expenses":expenses}

@app.post("/expenses") #accept post request
def add_expenses(expense: ExpenseSchema, db: Session=Depends(get_db)): 
    new_expense=models.Expense(
        category=expense.category,
        price=expense.price,
        date=expense.date
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return {"message": "Expense Added",  "expense": new_expense}


@app.get("/expenses/{category}") #{category}: path parameter
def get_by_category(category:str, db: Session=Depends(get_db)): #FastAPI automatically takes the value from the URL and passes it to this function as category
    expenses=db.query(models.Expense).filter(
        models.Expense.category.ilike(category)
    ).all()
    return {"expenses":expenses}

@app.delete("/expenses/{id}") #This defines a DELETE route, {index} is a path parameter
def delete_expense(id:int, db: Session=Depends(get_db)): #FastAPI takes the number from the URL and passes it to this function as index
    expense=db.query(models.Expense).filter(models.Expense.id == id).first()
    if expense:
        db.delete(expense)
        db.commit()
        return {"message": "Expense Deleted", "expense": expense} 
    return {"message" : "Invalid Index"}

@app.put("/expenses/{id}") #This defines an UPDATE route, {index} is path parameter 
def update_expense(id:int, updated: ExpenseSchema,db: Session= Depends(get_db)): 
    expense=db.query(models.Expense).filter(models.Expense.id==id).first()
    if expense:
        expense.category=updated.category
        expense.price=updated.price
        expense.date=updated.date
        db.commit()
        db.refresh(expense)
        return {
            "message":"Expense Updated", #notify that data updated
            "expense":expense #send updated data
        }
    return {"message":"Expense not found"}
