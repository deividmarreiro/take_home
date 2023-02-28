from fastapi import FastAPI
from app.routes import balance, event, reset

app = FastAPI()

app.include_router(balance.router)
app.include_router(event.router)
app.include_router(reset.router)