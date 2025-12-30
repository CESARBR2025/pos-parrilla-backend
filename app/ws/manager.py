from fastapi import WebSocket
import typing, asyncio

class ConnectionManager:  
    def __init__(self):
        self.active: typing.List[WebSocket] = []
        self.lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        async with self.lock:
            self.active.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        async with self.lock:
            if websocket in self.active:
                self.active.remove(websocket)

    async def broadcast(self, message: dict):
        async with self.lock:
            to_remove = []
            for ws in list(self.active):
                try:
                    await ws.send_json(message)  
                except Exception as e:
                    print("WS error:", e)
                    to_remove.append(ws)

            for r in to_remove:
                if r in self.active:
                    self.active.remove(r)
