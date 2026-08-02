"""STUB. Have I Been Pwned. Braucht Key -> nur aktiv, wenn Key gesetzt.
TODO: HTTP-Call gegen /breachedaccount/{email}, 6.5s Ratelimit beachten."""
from decimal import Decimal
from app.connectors.base import BaseConnector
from app.core.registry import register_connector
from app.core.config import settings
from app.schemas.connector import ConnectorCapability, RateLimit, RunContext
from app.schemas.enums import SelectorType, FindingType
from app.schemas.selector import SelectorOut
from app.schemas.finding import RawFinding


class HibpConnector(BaseConnector):
    capability = ConnectorCapability(
        name="hibp",
        version="0.1.0",
        accepts={SelectorType.EMAIL},
        produces={FindingType.BREACH},
        requires_auth=True,
        rate_limit=RateLimit(calls=1, per_seconds=7),
        cost_per_call_cents=Decimal("0.5"),
        reliability=0.95,
    )

    async def fetch(self, selector: SelectorOut, ctx: RunContext) -> list[RawFinding]:
        if not settings.hibp_api_key:
            return []
        # TODO: httpx GET https://haveibeenpwned.com/api/v3/breachedaccount/{email}
        #       Header hibp-api-key, User-Agent. 404 -> keine Leaks -> []
        raise NotImplementedError("HIBP-Fetch implementieren")


register_connector(HibpConnector())
