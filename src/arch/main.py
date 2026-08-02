"""FastAPI-App. In v1 optionaler zweiter Einstiegspunkt neben der CLI."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.registry import load_all
from app.core.db import init_db
from app.routes import run_routes, finding_routes, report_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_all()              # Connectoren + Agenten registrieren sich
    await init_db()
    yield


app = FastAPI(title="Footprint Self-Audit", lifespan=lifespan)
app.include_router(run_routes.router)
app.include_router(finding_routes.router)
app.include_router(report_routes.router)


@app.get("/health")
async def health():
    return {"status": "ok"}
