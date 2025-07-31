from fastapi import APIRouter, HTTPException
from models.spending import SpendingCreate, SpendingResponse
from uuid import uuid4
from datetime import datetime

router = APIRouter(prefix="/spending", tags=["Spending"])

# In-memory dummy DB (just for testing)
spending_db = []

@router.post("/", response_model=SpendingResponse)
def create_spending(spending: SpendingCreate):
    new_entry = SpendingResponse(
        id=str(uuid4()),
        user_id=spending.user_id,
        category=spending.category,
        amount=spending.amount,
        description=spending.description,
        date=spending.date or datetime.utcnow(),
        created_at=datetime.utcnow()
    )
    spending_db.append(new_entry)
    return new_entry

@router.get("/", response_model=list[SpendingResponse])
def list_spending():
    return spending_db
