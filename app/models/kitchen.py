from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

#Lo que manda la comanda
class KitchenOrderCreate(BaseModel):
    table_id: int
    product_id: UUID
    product_name: str
    quantity: int
    notes: Optional[str] = None

#Lo que vera cocina
class KitchenOrderOut(BaseModel):
    id: UUID
    table_id: int
    product_id: UUID
    product_name: str
    quantity: int
    notes: Optional[str]
    status: str
    created_at: datetime

#Actualizar estado
class KitchenOrderUpdateStatus(BaseModel):
    status:str
