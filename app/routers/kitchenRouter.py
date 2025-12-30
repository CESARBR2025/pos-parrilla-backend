#Valida request / response
#Llama al servicio
# Maneja  errores de HTTP
# No tiene logica de negocio

from fastapi import APIRouter, HTTPException
from uuid import UUID

from app.models.kitchen import (
    KitchenOrderCreate, KitchenOrderOut, KitchenOrderUpdateStatus
)

from app.services.kitchenService import (
    create_order_kitchen, get_kitchen_orders, update_kitchen_order_status
)

from app.ws.kitchenManager import kitchen_manager

#Base
router = APIRouter(
    prefix="/kitchen",
    tags=["Kitchen"]
)

#Post
@router.post("/orders", response_model=KitchenOrderOut, status_code=201)
async def send_to_kitchen(data: KitchenOrderCreate):
    try:
        order = create_order_kitchen(data)
        #Notificar en tiempo real 
        await kitchen_manager.broadcast({
            "type": "KITCHEN_ORDER_CREATED",
            "payload": order
        })
        return order
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))

#Get
@router.get("/orders",response_model=list[KitchenOrderOut])
def list_kitchen_orders():
    try:
        return get_kitchen_orders()
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

#Update status
@router.patch("/orders/{orderid}", response_model=KitchenOrderOut)
def change_kitchen_status(order_id: UUID, data: KitchenOrderUpdateStatus):
    try:
        return update_kitchen_order_status(
            order_id=str(order_id),
            status=data.status
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=404, detail=str(e))