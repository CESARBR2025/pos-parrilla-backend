# Servicio para logica de supabase

from app.db.supabase import client_supabase
from datetime import datetime
from typing import List, Dict
from app.models.table import TableOut


# Listar mesas
def list_tables() -> List[TableOut]:
    try:
        res = (
            client_supabase.table("tables")
            .select("*")
            .order("id", desc=False)
            .execute()
        )
        return res.data
    except Exception as e:
        raise RuntimeError(f"Error al listar mesas: {str(e)}")


def generate_tables(total: int) -> int:
    from datetime import datetime

    # Truncar todas las columnas
    try:
        client_supabase.rpc("restart_tables_sequence", {}).execute()
    except Exception as e:
        raise RuntimeError(f"Error resetting table IDs: {str(e)}")

    # 2. Crear nuevas mesas
    to_insert = []
    for i in range(1, total + 1):
        to_insert.append(
            {
                "name": f"Mesa {i}",
                "capacity": 4,
                "status": "libre",
                "updated_at": datetime.utcnow().isoformat(),
            }
        )

    # 3. Insertar todas
    try:
        res = client_supabase.table("tables").insert(to_insert).execute()
        return len(to_insert)  # número de mesas creadas
    except Exception as e:
        raise RuntimeError(f"Error generating tables: {str(e)}")


def updated_table_status(table_id: int, status: str) -> Dict:

    payload = {"status": status, "updated_at": datetime.utcnow().isoformat()}

    # actualizar
    client_supabase.table("tables").update(payload).eq("id", table_id).execute()

    # obtener registro actualizado
    res = client_supabase.table("tables").select("*").eq("id", table_id).execute()
    return res.data[0] if res.data else None
