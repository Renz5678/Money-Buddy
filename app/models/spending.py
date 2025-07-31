from pydantic import BaseModel, condecimal
from typing import Optional, Annotated
from datetime import datetime

AmountPositive = Annotated[condecimal(gt=0), ...]

class SpendingBase(BaseModel):
    category: str
    amount: AmountPositive
    description: Optional[str] = None
    date: Optional[datetime] = None

class SpendingCreate(SpendingBase):
    user_id: str

class SpendingResponse(SpendingBase):
    id: str
    user_id: str
    created_at: datetime
