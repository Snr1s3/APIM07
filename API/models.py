from pydantic import BaseModel
from datetime import date

class IncomeBase(BaseModel):
    title: str
    description: str
    amount: float
    date: date

class IncomeCreate(IncomeBase):
    pass

class Income(IncomeBase):
    id: int

    class Config:
        from_attributes = True

class ExpenseBase(BaseModel):
    title: str
    description: str
    amount: float
    date: date

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int

    class Config:
        from_attributes = True