from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import tables
from app.ws import tables_ws
from app.core.config import FRONTEND_ORIGINS

app = FastAPI(title="POS BACKEND")

app.add_middleware(
  CORSMiddleware,
  allow_origins=FRONTEND_ORIGINS,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.include_router(tables.router)
app.include_router(tables_ws.router)