# Son tipado, validación, estrcutura de entrada-salia
# Sirven para: definir que recibe endpoint y que devuelve
# Prueba de commiteo

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


# Contener los campos comunes
class ProductBase(BaseModel):
    name: str
    group_id: str
    is_active: bool


# Para crear un grupo
class ProductCreate(ProductBase):
    pass


# Update simple
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    group_id: Optional[str] = None
    is_active: Optional[bool] = None


# Update extendido mas campos
class ProductUpdateExtended(BaseModel):
    name: Optional[str] = None
    group_id: Optional[str] = None
    is_active: Optional[bool] = None
    order_id: Optional[int] = None


# Forma final
class ProductOut(ProductBase):
    id: UUID
    order_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
