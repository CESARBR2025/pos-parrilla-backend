# Son tipado, validación, estrcutura de entrada-salia
# Sirven para: definir que recibe endpoint y que devuelve
# Prueba de commiteo

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


# Contener los campos comunes
class GroupBase(BaseModel):
    name: str
    is_active: bool


# Para crear un grupo
class GroupCreate(GroupBase):
    pass


# Update simple
class GroupUpdate(BaseModel):
    name: Optional[str] = None
    is_active: Optional[bool] = None


# Update extendido mas campos
class GroupUpdateExtended(BaseModel):
    name: Optional[str] = None
    is_active: Optional[bool] = None
    order_id: Optional[int] = None


# Forma final
class GroupOut(GroupBase):
    id: UUID
    order_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
