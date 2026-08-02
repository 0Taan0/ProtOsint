from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_session

router = APIRouter(prefix="/runs/{run_id}/report", tags=["report"])


@router.get("")
async def get_report(run_id: UUID, session: AsyncSession = Depends(get_session)):
    # TODO: report_service -> HTML / JSON
    raise NotImplementedError
