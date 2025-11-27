from  pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TableBase(BaseModel):
  name: str
  capacity: int = 4

class TableCreate(TableBase):
  pass

class TableUpdateStatus(BaseModel):
  status: str

class TableOut(TableBase):
  id: int
  status: str
  created_at: Optional[datetime] = None
  updated_at: Optional[datetime] = None
  
  class Config:
    orm_mode = True