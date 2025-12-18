#Declara un router de WS
#Usa el manager para mantener la conexion viva
#Recibe mensajes
#Envia mensajes en tiempo real

from fastapi import APIRouter,WebSocket, WebSocketDisconnect
import json
from app.ws.manager import manager

router = APIRouter(prefix="/ws/tables", tags=["Tables"])

@router.websocket("/")
async def ws_tables(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            raw = await websocket.receive_text()
            message = json.loads(raw)

            event = message.get("event")
            data = message.get("data")

            if event == "table_updated":
                print("La mesa fue actualizada:", data)
                await websocket.send_text(json.dumps({
                    "status": "ok",
                    "message": "Evento recibido",
                    "data": data
                }))
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
