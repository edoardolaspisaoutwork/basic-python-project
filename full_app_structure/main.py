from fastapi import FastAPI
from full_app_structure.routers import items

app = FastAPI(title="FastAPI Project")

app.include_router(items.router, prefix="/api/items", tags=["Items"])
