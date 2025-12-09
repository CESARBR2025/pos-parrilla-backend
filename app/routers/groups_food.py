from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.group_schema import FoodGroupBase, FoodGroupCreate, FoodGroupUpdate, FoodGroupOut
from app.services.food_groups_service import list_food_groups, create_group_food, updated_group_food_status
from app.ws.manager import manager
import json
from uuid import UUID

router = APIRouter(prefix="/foodgroups", tags=["FoodGroups"])

@router.get("/", response_model=List[FoodGroupOut])
def get_group_food():
    try:
        return list_food_groups()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generateGroup")
async def post_generate_group_food(name: str, order_id: int):
  import asyncio
  try:
    added = create_group_food(name, order_id)
    #after generation send fresh list
    groups = list_food_groups()
    await manager.broadcast(json.dumps({"event": "groups_generated", "data": groups}))

    return {"added": added}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
  
@router.patch("/{id}/status", response_model=FoodGroupOut)
async def patch_group_food_status(id: UUID, payload: FoodGroupUpdate):
  try:
    data_to_update = payload.dict(exclude_unset=True)
    updated = updated_group_food_status(id, data_to_update)
    #notify via ws
    await manager.broadcast(json.dumps({"event": "group_updated", "data": updated}))
    return updated
  except KeyError:
    raise HTTPException(status_code=404, detail="Group not found")
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))