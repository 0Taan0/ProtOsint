"""Der Connector-Contract. Dies ist die Naht zur Außenwelt."""
from decimal import Decimal
from typing import Protocol, ClassVar, runtime_checkable
from pydantic import BaseModel, Field
from app.schemas.enums import SelectorType, FindingType
from app.schemas.selector import SelectorOut
from app.schemas.finding import RawFinding


class RateLimit(BaseModel):
    calls: int = 60
    per_seconds: int = 60


class ConnectorCapability(BaseModel):
    """Selbstauskunft eines Connectors. Der Orchestrator matcht damit,
    welche Connectoren fuer einen Selektor ueberhaupt in Frage kommen."""
    name: str
    version: str
    accepts: set[SelectorType]
    produces: set[FindingType]
    requires_auth: bool = False
    rate_limit: RateLimit = Field(default_factory=RateLimit)
    cost_per_call_cents: Decimal = Decimal("0")
    reliability: float = Field(default=0.5, ge=0, le=1)   # Prior fuer Confidence


class RunContext(BaseModel):
    """Wird jedem Connector-Aufruf mitgegeben. Read-only fuer den Connector."""
    run_id: str
    offline: bool = False                 # nur Cache, kein Netz
    budget_remaining_cents: Decimal = Decimal("0")


@runtime_checkable
class Connector(Protocol):
    """Jeder Connector implementiert genau das hier. Mehr nicht."""
    capability: ClassVar[ConnectorCapability]

    async def run(self, selector: SelectorOut, ctx: RunContext) -> list[RawFinding]:
        ...
