# Servicio para operaciones en BD

from app.db.supabase import client_supabase
from datetime import datetime
from typing import List, Dict
from app.models.foodGroupModel import (
    GroupOut,
    GroupUpdate,
    GroupUpdateExtended,
    GroupCreate,
)
from uuid import UUID


# listar grupos
def list_foodGroup() -> List[GroupOut]:
    try:
        res = (
            client_supabase.table("food_group")
            .select("*")
            .order("id", desc=False)
            .execute()
        )
        return res.data
    except Exception as e:
        raise RuntimeError(f"Error al listar las mesas: {str(e)}")


# Generar grupo
def create_foodGroup(data: GroupCreate) -> GroupOut:

    # Traer el ultimo order_id
    res = (
        client_supabase.table("food_group")
        .select("order_id")
        .order("order_id", desc=True)
        .limit(1)
        .execute()
    )
    last_order = res.data[0]["order_id"] if res.data else 0

    try:
        payload = {
            "name": data.name,
            "is_active": data.is_active,
            "order_id": last_order + 1,
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat(),
        }

        res = client_supabase.table("food_group").insert(payload).execute()

        return res.data[0]
    except Exception as e:
        raise RuntimeError(f"Error al crear grupo: {str(e)}")


# Actualizar name + is_active PATCH
def update_food_group(group_id: UUID, data: GroupUpdate) -> GroupOut:
    try:
        payload = data.dict(exclude_unset=True)
        payload["updated_at"] = datetime.utcnow().isoformat()

        res = (
            client_supabase.table("food_group")
            .update(payload)
            .eq("id", str(group_id))
            .execute()
        )

        if not res.data:
            raise ValueError("Grupo no encontrado")

        return res.data[0]
    except Exception as e:
        raise RuntimeError(f"Error al actualizar grupo: {str(e)}")


# Update avanzado mas campos
def update_food_group_extended(group_id: UUID, data: GroupUpdateExtended) -> GroupOut:
    try:
        payload = data.dict(exclude_unset=True)
        payload["updated_at"] = datetime.utcnow().isoformat()

        res = (
            client_supabase.table("food_group")
            .update(payload)
            .eq("id", str(group_id))
            .execute()
        )

        if not res.data:
            raise ValueError("Grupo no encontrado")

        return res.data[0]
    except Exception as e:
        raise RuntimeError(f"Error al actualizar grupo: {str(e)}")


# Obtener grupo por ID
def get_food_group_by_id(group_id: UUID) -> GroupOut:
    try:
        res = (
            client_supabase.table("food_group")
            .select("*")
            .eq("id", str(group_id))
            .single()
            .execute()
        )

        return res.data
    except Exception as e:
        raise RuntimeError(f"Grupo no encotrnado: {str(e)}")
