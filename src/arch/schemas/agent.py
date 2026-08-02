"""Der Agent-Contract. Agenten schlagen vor, sie schreiben nie direkt."""
from uuid import UUID
from typing import Protocol, ClassVar, runtime_checkable
from pydantic import BaseModel, Field
from app.schemas.enums import ProposalKind, Phase


class Proposal(BaseModel):
    """Ein Vorschlag eines Agenten. Wird vom Applier geprueft und erst
    dann angewendet. evidence ist Pflicht -> blockiert Halluzination."""
    kind: ProposalKind
    payload: dict
    confidence: float = Field(ge=0, le=1)
    evidence: list[UUID] = Field(min_length=1)     # existierende Finding-IDs
    rationale: str = Field(max_length=400)


class AgentResult(BaseModel):
    proposals: list[Proposal] = Field(default_factory=list)
    tokens_used: int = 0


class AgentContext(BaseModel):
    """Vorselektierte Evidenz plus Metadaten. Der Agent bekommt NIE den
    ganzen Graphen, sondern eine deterministisch gefilterte Menge."""
    run_id: str
    phase: Phase
    subject_id: UUID
    evidence_ids: list[UUID] = Field(default_factory=list)
    payload: dict = Field(default_factory=dict)    # phasenabhaengiger Input


@runtime_checkable
class Agent(Protocol):
    name: ClassVar[str]
    phase: ClassVar[Phase]

    async def run(self, ctx: AgentContext) -> AgentResult:
        ...
