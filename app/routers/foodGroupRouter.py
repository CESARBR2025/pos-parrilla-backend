# Declaración de endpoints para consukltar grupos

from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from app.models.foodGroupModel import (
    GroupOut,
    GroupUpdate,
    GroupUpdateExtended,
    GroupCreate,
)
from app.services.food_group_service import (
    list_foodGroup,
    create_foodGroup,
    update_food_group,
    update_food_group_extended,
    get_food_group_by_id,
)


from app.ws.manager import manager
import json

router = APIRouter(prefix="/foodGroup", tags=["FoodGroups"])


@router.get("/", response_model=List[GroupOut])
def get_groupFood():
    try:
        return list_foodGroup()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Crear grupo
@router.post("/", response_model=GroupOut)
def create_group(data: GroupCreate):
    try:
        return create_foodGroup(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# PATCH simple
@router.patch("/{group_id}", response_model=GroupOut)
def patch_group(group_id: UUID, data: GroupUpdate):
    try:
        return update_food_group(group_id, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# PATCH avanzado
@router.patch("/{group_id}/advanced", response_model=GroupOut)
def patch_group(group_id: UUID, data: GroupUpdateExtended):
    try:
        return update_food_group_extended(group_id, data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# GET By ID
@router.get("/{group_id}", response_model=GroupOut)
def get_group(group_id: UUID):
    try:
        return get_food_group_by_id(group_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
