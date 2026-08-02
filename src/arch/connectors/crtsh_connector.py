"""STUB. Certificate Transparency via crt.sh. Kostenlos, kein Key.
TODO: GET https://crt.sh/?q=%25.{domain}&output=json -> Subdomains extrahieren."""
from app.connectors.base import BaseConnector
from app.core.registry import register_connector
from app.schemas.connector import ConnectorCapability, RunContext
from app.schemas.enums import SelectorType, FindingType
from app.schemas.selector import SelectorOut
from app.schemas.finding import RawFinding


class CrtShConnector(BaseConnector):
    capability = ConnectorCapability(
        name="crtsh",
        version="0.1.0",
        accepts={SelectorType.DOMAIN},
        produces={FindingType.DOMAIN_RECORD},
        reliability=0.9,
    )

    async def fetch(self, selector: SelectorOut, ctx: RunContext) -> list[RawFinding]:
        # TODO: httpx GET crt.sh, JSON parsen, dedupe common_name/name_value
        #       Subdomains koennen neue URL/DOMAIN-Selektoren produzieren
        raise NotImplementedError("crt.sh-Fetch implementieren")


register_connector(CrtShConnector())
