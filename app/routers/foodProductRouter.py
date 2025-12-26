from fastapi import APIRouter
from uuid import UUID
from typing import List

from app.models.foodProductModel import ProductOut
from app.services.food_product_service import list_foodProduct

router = APIRouter(
    prefix="/foodproducts",
    tags=["Food Products"]
)

@router.get("/{group_Id}/product", response_model=list[ProductOut])
def get_products_by_group(group_id: UUID):
    return list_foodProduct(group_id)

