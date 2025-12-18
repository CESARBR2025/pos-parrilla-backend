# Son tipado, validacion, estructura de entrada/salida
# Sirven para: definir que recibe un endpoint, que devuelve, validar datos, documentar en swagger

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Contener los campos comunnes en una clase
class TableBase(BaseModel):
    name: str
    capacity: int = 4


# Para crear una table
class TableCreate(TableBase):
    pass


class TableUpdateStatus(BaseModel):
    status: str


# Heradar los campos comunes
class TableOut(TableBase):
    id: int
    status: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
