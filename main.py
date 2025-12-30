from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import tablesRouter, foodGroupRouter, foodProductRouter, kitchenRouter
from app.ws import tables_ws
from app.core.config import FRONTEND_ORIGINS

app = FastAPI(title="POS BACKEND")

app.add_middleware(
    CORSMiddleware,
    allow_origins=FRONTEND_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tablesRouter.router)
app.include_router(tables_ws.router)
app.include_router(foodGroupRouter.router)
app.include_router(foodProductRouter.router)
app.include_router(kitchenRouter.router)
