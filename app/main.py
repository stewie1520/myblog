from fastapi import FastAPI

from .routers import items, files

app = FastAPI()


app.include_router(
    items.router,
    prefix="/items",
    tags=["items"],
)

app.include_router(
    files.router,
    prefix="/files",
    tags=["files"]
)
