"""Zweiter Einstiegspunkt neben der CLI -- ruft dieselben Services."""
from uuid import UUID
from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_session
from app.schemas.selector import SelectorIn

router = APIRouter(prefix="/runs", tags=["runs"])


@router.post("")
async def create_run(seeds: list[SelectorIn], bg: BackgroundTasks,
                     session: AsyncSession = Depends(get_session)):
    # TODO: Subject sicherstellen, Run + Seed-Selektoren + Tasks anlegen,
    #       bg.add_task(orchestration_service.run_audit, run, session)
    raise NotImplementedError


@router.get("/{run_id}")
async def get_run(run_id: UUID, session: AsyncSession = Depends(get_session)):
    # TODO: Run-Status + Phase zurueckgeben
    raise NotImplementedError
