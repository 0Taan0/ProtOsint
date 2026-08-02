"""STUB. Baut den HTML-Report aus RiskItems + Risk-Agent-Text."""
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.run import Run
from app.schemas.report import Report


async def build_report(run: Run, session: AsyncSession) -> Report:
    # TODO: RiskItems laden, nach score sortieren, HTML rendern, Pfad zurueckgeben
    raise NotImplementedError
