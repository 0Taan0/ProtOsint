"""STUB. Entity Resolution + Graph. Deterministische Kanten (gleiche Mail,
gleicher Avatar-Hash) hier; unsichere Kanten kommen vom Attribution-Agenten."""
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.run import Run


async def resolve_entities(run: Run, session: AsyncSession) -> None:
    # TODO: Findings zu Entities clustern, deterministische Edges anlegen
    raise NotImplementedError


async def shortest_chain(run_id, session: AsyncSession) -> float:
    """Kuerzester Pfad Pseudonym -> Klarname-Attribut. Rekursive CTE ueber edges.
    Liefert den chain_score fuers Scoring."""
    # TODO: WITH RECURSIVE ... ueber edges
    raise NotImplementedError
