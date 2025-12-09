from app.db.supabase import client_supabase
from typing import List, Dict
from datetime import datetime

def list_food_groups() -> List[Dict]:
    try:
        res = (
            client_supabase
            .table("food_group")
            .select("*")
            .order("id", desc=False)
            .execute()
        )
        return res.data
    except Exception as e:
        raise RuntimeError(f"Error al listar los datos: str{e}")
    

def create_group_food(name: str, order_id: int = 0) -> Dict:
  payload = {"name": name, "order_id": order_id, "is_active": True, "created_at": datetime.utcnow().isoformat()}
  try:
    res = client_supabase.table("food_group").insert(payload).execute()
    return res.data
  except Exception as e:
    raise RuntimeError(f"Error al crear grupo de alimentos: {str(e)}")



def updated_group_food_status(id: int, data: dict ) -> Dict:
    

    # actualizar
    client_supabase.table("food_group").update(data).eq("id", id).execute()

    # obtener registro actualizado
    res = client_supabase.table("food_group").select("*").eq("id", id).execute()
    return res.data[0] if res.data else None
    
  
