from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_session

router = APIRouter(prefix="/runs/{run_id}/findings", tags=["findings"])


@router.get("")
async def list_findings(run_id: UUID, session: AsyncSession = Depends(get_session)):
    # TODO: Findings des Runs, optional nach type/verified filtern
    raise NotImplementedError
