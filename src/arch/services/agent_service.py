"""Bindeglied Registry <-> Applier <-> AgentLog. Fuehrt alle Agenten einer
Phase aus, protokolliert und uebergibt die Proposals an den Applier."""
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.registry import agents_for
from app.schemas.enums import Phase
from app.schemas.agent import AgentContext
from app.models.run import Run
from app.services import apply_service
from app.core.logging import get_logger

log = get_logger("agent_service")


async def run_phase(phase: Phase, run: Run, session: AsyncSession) -> None:
    for agent in agents_for(phase):
        ctx = await _build_context(agent, phase, run, session)   # deterministische Evidenz-Vorauswahl
        result = await agent.run(ctx)
        outcome = await apply_service.apply(result.proposals, run, session)
        await _log(agent.name, run, result, outcome, session)


async def _build_context(agent, phase: Phase, run: Run, session: AsyncSession) -> AgentContext:
    # TODO: pro Phase die passende Evidenz per SQL vorselektieren (Top-N nach
    #       Prefilter), NIE den ganzen Graphen. evidence_ids fuellen.
    return AgentContext(run_id=str(run.id), phase=phase, subject_id=run.subject_id)


async def _log(name, run, result, outcome, session) -> None:
    # TODO: AgentLog-Zeile mit raw_response, accepted, rejected, tokens schreiben
    pass
