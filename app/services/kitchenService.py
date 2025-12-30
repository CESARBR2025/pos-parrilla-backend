from datetime import datetime
from supabase import Client

from app.models.kitchen import KitchenOrderCreate
from app.db.supabase import client_supabase

#Crear orden de cocina
def create_order_kitchen(data: KitchenOrderCreate):
    try:
        payload = {
            "table_id": data.table_id,
            "product_id": str(data.product_id),
            "product_name": data.product_name,
            "quantity": data.quantity,
            "notes": data.notes,
            "status": "PENDING",
            "created_at": datetime.utcnow().isoformat()
        }

        res = (client_supabase.table("kitchen_orders").insert(payload).execute())

        return res.data[0]
    except Exception as e:
        raise RuntimeError(f"Error al crear la orden en cocina: {str(e)}")
    

#Obtener ordenes de cocina
def get_kitchen_orders():
    try:
        res = (
            client_supabase.
            table("kitchen_orders")
            .select("*")
            .neq("status", "READY")
            .order("created_at")
            .execute()
        )

        return res.data
    except Exception as e:
        raise RuntimeError(f"Error al obtener órdenes de cocina: {str(e)}")
    

#Actualizar estado de cocina
def update_kitchen_order_status(order_id: str, status: str):
    if status not in ["PENDING", "IN_PROGRESS", "READY"]:
        raise ValueError("Estado de cocina invalido")
    
    try:
        res = (
            client_supabase
            .table("kitchen_orders")
            .update({
                "status": status,
            })
            .eq("id", order_id)
            .execute()
        )

        if not res.data:
            raise RuntimeError ("Orden no encontrada")
        
        return res.data[0]
    except Exception as e:
        raise RuntimeError(f"Error al actualizar estado de cocina: {str(e)}")
    
