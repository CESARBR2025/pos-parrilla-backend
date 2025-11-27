from fastapi import APIRouter,WebSocket, WebSocketDisconnect
import json
from app.ws.manager import manager

router = APIRouter(prefix="/ws/tables", tags=["Tables"])

@router.websocket("/")
async def ws_tables(websocket: WebSocket):
  await manager.connect(websocket)
  try:
    while True:
      #keep connection alive; frontend may send pings
      data = await WebSocket.receive_text()
      #optionally handle messages from clients if neded
  except WebSocketDisconnect:
    await manager.disconnect(websocket)