from pydantic import BaseModel, condecimal
from typing import Optional, Annotated
from datetime import datetime

# Define reusable annotated types
PositiveDecimal = Annotated[condecimal(gt=0), ...]
NonNegativeDecimal = Annotated[condecimal(ge=0), ...]

class BudgetBase(BaseModel):
    month: str  # e.g. "July 2025"
    income: PositiveDecimal
    expenses: NonNegativeDecimal
    savings_goal: Optional[NonNegativeDecimal] = 0

class BudgetCreate(BudgetBase):
    user_id: str

class BudgetResponse(BudgetBase):
    id: str
    user_id: str
    created_at: datetime
