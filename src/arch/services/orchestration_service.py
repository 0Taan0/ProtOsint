"""LAUFFAEHIGE VERDRAHTUNG (Skelett). Der Supervisor als Zustandsautomat.
Kein Agent entscheidet ueber den naechsten Schritt -- der Loop tut es,
rein mechanisch. Die einzelnen Phasen rufen Services/Registry und sind
als TODO markiert, aber der Kontrollfluss steht komplett."""
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.run import Run
from app.schemas.enums import Phase, RunStatus
from app.core.logging import get_logger
from app.services import (
    collection_service, verification_service, correlation_service,
    scoring_service, report_service,
)
from app.services import agent_service

log = get_logger("orchestrator")

# Lineare Phasenfolge. Der COLLECT/VERIFY-Block ist der Pivot-Loop.
_LINEAR = [Phase.DISCOVER, Phase.COLLECT, Phase.VERIFY, Phase.ANALYZE,
           Phase.CORRELATE, Phase.SCORE, Phase.REPORT]


async def run_audit(run: Run, session: AsyncSession) -> None:
    run.status = RunStatus.RUNNING
    await session.commit()
    try:
        await _discover(run, session)
        await _pivot_loop(run, session)          # COLLECT + VERIFY, mehrfach
        await _analyze(run, session)
        await _correlate(run, session)
        await _score(run, session)
        await _report(run, session)
        run.status = RunStatus.DONE
    except Exception as e:
        log.exception("audit failed")
        run.status = RunStatus.FAILED
    finally:
        await session.commit()


async def _pivot_loop(run: Run, session: AsyncSession) -> None:
    """Die Rueckkopplung aus dem Diagramm. Endet MECHANISCH:
    Budget erschoepft ODER Maximaltiefe ODER keine neuen Selektoren mehr."""
    depth = 0
    while depth <= run.max_depth:
        if run.budget_spent >= run.budget_cents:
            log.info("budget exhausted at depth %d", depth); break
        run.phase = Phase.COLLECT
        produced = await collection_service.collect_open_tasks(run, session)   # Connectoren
        run.phase = Phase.VERIFY
        outcome = await verification_service.verify_new_findings(run, session)  # Attribution-Agent
        if outcome.new_selectors_count() == 0:
            log.info("no new selectors at depth %d -> stop", depth); break
        depth += 1


async def _discover(run: Run, session: AsyncSession) -> None:
    run.phase = Phase.DISCOVER
    await agent_service.run_phase(Phase.DISCOVER, run, session)   # Discovery-Agent -> Selektoren

async def _analyze(run: Run, session: AsyncSession) -> None:
    run.phase = Phase.ANALYZE
    await agent_service.run_phase(Phase.ANALYZE, run, session)    # Analysis-Agent

async def _correlate(run: Run, session: AsyncSession) -> None:
    run.phase = Phase.CORRELATE
    await correlation_service.resolve_entities(run, session)      # deterministisch

async def _score(run: Run, session: AsyncSession) -> None:
    run.phase = Phase.SCORE
    await scoring_service.score_run(run, session)                 # deterministisch

async def _report(run: Run, session: AsyncSession) -> None:
    run.phase = Phase.REPORT
    await agent_service.run_phase(Phase.REPORT, run, session)     # Risk-Agent (nur Text)
    await report_service.build_report(run, session)
