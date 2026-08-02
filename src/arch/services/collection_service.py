"""STUB. Fuehrt offene Tasks aus: pro Selektor die passenden Connectoren
(aus der Registry), normalisiert die RawFindings und persistiert sie."""
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.run import Run
from app.core.registry import connectors_for
from app.services import normalization_service   # noqa


async def collect_open_tasks(run: Run, session: AsyncSession) -> int:
    """Gibt die Anzahl neu erzeugter Findings zurueck."""
    # TODO:
    #  1. offene Tasks des Runs laden (status=pending)
    #  2. je Task: connectors_for(selector.type), parallel via asyncio.TaskGroup
    #  3. RawFindings -> normalization_service.persist(...) (setzt fingerprint, provenance)
    #  4. Task-Status + run.budget_spent fortschreiben
    raise NotImplementedError("collection_service ausbauen")
