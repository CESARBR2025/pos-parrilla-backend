from app.db.supabase import client_supabase
from datetime import datetime
from typing import List, Dict
from app.models.foodProductModel import (
    ProductOut, ProductUpdate, ProductUpdateExtended, ProductCreate
)

from uuid import UUID

#Listar productos
def list_foodProduct(group_id: UUID) -> List[ProductOut]:
    try:
        res = (
            client_supabase.table("food_product")
            .select("*")
            .eq("group_id", str(group_id))
            .eq("is_active", True)
            .order("order_id")
            .execute()
        )
        return [ProductOut(**item) for item in res.data]
    except Exception as e:
        raise RuntimeError(f"Error al listar productos: {str(e)}")