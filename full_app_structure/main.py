from fastapi import FastAPI
from full_app_structure.routers import item_router

app = FastAPI(title="FastAPI Project")

app.include_router(item_router.router)
#app.include_router(item_router.router, prefix="/api/items", tags=["Items"])

