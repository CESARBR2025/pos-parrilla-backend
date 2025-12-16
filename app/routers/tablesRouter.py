from fastapi import APIRouter, HTTPException
from typing import List
from app.models.table import TableCreate, TableOut, TableUpdateStatus
from app.services.table_service import (
    list_tables,
    generate_tables,
    updated_table_status,
)
from app.ws.manager import manager
import json

router = APIRouter(prefix="/tables", tags=["Tables"])


@router.get("/", response_model=List[TableOut])
def get_tables():
    try:
        return list_tables()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate")
async def post_generate(total: int):
    import asyncio

    try:
        added = generate_tables(total)
        # after generation send fresh list
        tables = list_tables()
        await manager.broadcast(
            json.dumps({"event": "tables_generated", "data": tables})
        )

        return {"added": added, "total_expected": total}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/{table_id}/status", response_model=TableOut)
async def patch_table_status(table_id: int, payload: TableUpdateStatus):
    try:
        updated = updated_table_status(table_id, payload.status)
        # notify via ws
        await manager.broadcast(json.dumps({"event": "table_updated", "data": updated}))
        return updated
    except KeyError:
        raise HTTPException(status_code=404, detail="Table not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
