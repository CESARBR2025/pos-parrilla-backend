from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.ws.controlers.kitchenManager import kitchen_manager

router = APIRouter()


@router.websocket("/ws/kitchen")
async def kitchen_ws(websocket: WebSocket):
    

    await kitchen_manager.connect(websocket)
    
    try:
        while True:
            await websocket.receive_text() #mantiene viva la conexion
    except WebSocketDisconnect:
        kitchen_manager.disconnect(websocket)