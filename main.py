from fastapi import FastAPI
from app.routers import ubibot

app = FastAPI(title="Ubi API");

app.include_router(ubibot.router);