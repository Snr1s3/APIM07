from fastapi import FastAPI, HTTPException, Depends
from .client import get_db_connection
from .models import IncomeCreate, Income, ExpenseCreate, Expense
from datetime import date
import mysql.connector

app = FastAPI()

# CRUD for Incomes
@app.post("/incomes/", response_model=Income)
def create_income(income: IncomeCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO incomes (title, description, amount, date) VALUES (%s, %s, %s, %s)",
            (income.title, income.description, income.amount, income.date),
        )
        conn.commit()
        income_id = cursor.lastrowid
    except mysql.connector.Error as err:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(err))
    finally:
        cursor.close()
        conn.close()
    return {**income.dict(), "id": income_id}

@app.get("/incomes/{income_id}", response_model=Income)
def read_income(income_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM incomes WHERE id = %s", (income_id,))
    income = cursor.fetchone()
    cursor.close()
    conn.close()
    if not income:
        raise HTTPException(status_code=404, detail="Income not found")
    return income

@app.get("/incomes/", response_model=list[Income])
def read_incomes(skip: int = 0, limit: int = 10):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM incomes LIMIT %s OFFSET %s", (limit, skip))
    incomes = cursor.fetchall()
    cursor.close()
    conn.close()
    return incomes

@app.put("/incomes/{income_id}", response_model=Income)
def update_income(income_id: int, income: IncomeCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE incomes SET title = %s, description = %s, amount = %s, date = %s WHERE id = %s",
            (income.title, income.description, income.amount, income.date, income_id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Income not found")
    except mysql.connector.Error as err:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(err))
    finally:
        cursor.close()
        conn.close()
    return {**income.dict(), "id": income_id}

@app.delete("/incomes/{income_id}", response_model=dict)
def delete_income(income_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM incomes WHERE id = %s", (income_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Income deleted successfully"}

# CRUD for Expenses
@app.post("/expenses/", response_model=Expense)
def create_expense(expense: ExpenseCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO expenses (title, description, amount, date) VALUES (%s, %s, %s, %s)",
            (expense.title, expense.description, expense.amount, expense.date),
        )
        conn.commit()
        expense_id = cursor.lastrowid
    except mysql.connector.Error as err:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(err))
    finally:
        cursor.close()
        conn.close()
    return {**expense.dict(), "id": expense_id}

@app.get("/expenses/{expense_id}", response_model=Expense)
def read_expense(expense_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM expenses WHERE id = %s", (expense_id,))
    expense = cursor.fetchone()
    cursor.close()
    conn.close()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@app.get("/expenses/", response_model=list[Expense])
def read_expenses(skip: int = 0, limit: int = 10):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM expenses LIMIT %s OFFSET %s", (limit, skip))
    expenses = cursor.fetchall()
    cursor.close()
    conn.close()
    return expenses

@app.put("/expenses/{expense_id}", response_model=Expense)
def update_expense(expense_id: int, expense: ExpenseCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE expenses SET title = %s, description = %s, amount = %s, date = %s WHERE id = %s",
            (expense.title, expense.description, expense.amount, expense.date, expense_id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Expense not found")
    except mysql.connector.Error as err:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(err))
    finally:
        cursor.close()
        conn.close()
    return {**expense.dict(), "id": expense_id}

@app.delete("/expenses/{expense_id}", response_model=dict)
def delete_expense(expense_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Expense deleted successfully"}

@app.get("/login/")
def login(username: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {user["id"]}

@app.get("/register/")
def register(username: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password),
        )
        conn.commit()
        user_id = cursor.lastrowid
    except mysql.connector.Error as err:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(err))
    finally:
        cursor.close()
        conn.close()
    return {"message": "User registered successfully", "user_id": user_id}