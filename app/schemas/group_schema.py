from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FoodGroupBase(BaseModel):
    name: str
    order_id: int

class FoodGroupCreate(FoodGroupBase):
    pass

class FoodGroupUpdate(BaseModel):
    name: Optional[str] = None
    order_id: Optional[int] = None
    is_active: Optional[bool] = None

class FoodGroupOut(FoodGroupBase):
    id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True