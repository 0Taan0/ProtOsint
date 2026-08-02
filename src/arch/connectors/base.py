"""Gemeinsame Connector-Basis: Cache- und Ratelimit-Wrapper, damit jeder
Connector nur noch fetch() implementiert und Cache/Netz automatisch bekommt."""
from abc import ABC, abstractmethod
from app.schemas.connector import ConnectorCapability, RunContext
from app.schemas.selector import SelectorOut
from app.schemas.finding import RawFinding
from app.core.ratelimit import TokenBucket
from app.core.logging import get_logger

log = get_logger("connector")


class BaseConnector(ABC):
    capability: ConnectorCapability

    def __init__(self) -> None:
        rl = self.capability.rate_limit
        self._bucket = TokenBucket(rl.calls, rl.per_seconds)

    async def run(self, selector: SelectorOut, ctx: RunContext) -> list[RawFinding]:
        # TODO(cache): hier cache_service.get(key) vorschalten (offline == nur Cache)
        # TODO(budget): Kosten gegen ctx.budget_remaining_cents pruefen
        if not ctx.offline:
            await self._bucket.acquire()
        try:
            findings = await self.fetch(selector, ctx)
        except Exception as e:                       # ein Connector-Fehler killt nie den Lauf
            log.warning("connector %s failed: %s", self.capability.name, e)
            return []
        # TODO(cache): Ergebnis in cache_service.set(key, ...)
        return findings

    @abstractmethod
    async def fetch(self, selector: SelectorOut, ctx: RunContext) -> list[RawFinding]:
        ...
