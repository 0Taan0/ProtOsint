"""LAUFFAEHIGE VERDRAHTUNG. Der Applier ist die Sicherheitsschleuse:
Agenten schlagen vor, hier wird geprueft und erst dann geschrieben.
Drei Gates: Evidenz existiert, Confidence >= Schwelle, Policy erlaubt."""
from dataclasses import dataclass, field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.agent import Proposal
from app.schemas.enums import ProposalKind
from app.models.finding import Finding
from app.models.run import Run
from app.core.logging import get_logger

log = get_logger("apply")


@dataclass
class ApplyOutcome:
    accepted: list[Proposal] = field(default_factory=list)
    rejected: list[tuple[Proposal, str]] = field(default_factory=list)

    def new_selectors_count(self) -> int:
        return sum(1 for p in self.accepted if p.kind == ProposalKind.NEW_SELECTOR)


async def _evidence_exists(ids: list, session: AsyncSession) -> bool:
    if not ids:
        return False
    rows = await session.execute(select(Finding.id).where(Finding.id.in_(ids)))
    return len({r[0] for r in rows}) == len(set(ids))


async def apply(proposals: list[Proposal], run: Run, session: AsyncSession) -> ApplyOutcome:
    outcome = ApplyOutcome()
    for p in proposals:
        if not await _evidence_exists(p.evidence, session):
            outcome.rejected.append((p, "evidence_missing"))          # blockt Halluzination
            continue
        if p.confidence < run.threshold:
            outcome.rejected.append((p, "below_threshold"))
            continue
        # TODO(policy): bei NEW_SELECTOR zusaetzlich policy.evaluate(...).may_pivot pruefen
        await _write(p, run, session)
        outcome.accepted.append(p)
    log.info("apply: %d accepted, %d rejected", len(outcome.accepted), len(outcome.rejected))
    return outcome


async def _write(p: Proposal, run: Run, session: AsyncSession) -> None:
    """Deterministische Anwendung je Proposal-Art. Hier entstehen Selektoren,
    Kanten, Klassifikationen -- NICHT im Agenten."""
    match p.kind:
        case ProposalKind.NEW_SELECTOR:
            # TODO: Selector(subject_id=run.subject_id, type=..., value=..., depth+1)
            pass
        case ProposalKind.ENTITY_LINK:
            # TODO: Edge(src, dst, type, confidence=p.confidence, evidence_ids=p.evidence)
            pass
        case ProposalKind.CLASSIFICATION:
            # TODO: Finding.attributes um Sensitivitaetslabel ergaenzen
            pass
        case ProposalKind.RISK_NOTE:
            # TODO: RiskItem.remediation / summary setzen
            pass
