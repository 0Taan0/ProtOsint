"""STUB. Username-Discovery ueber viele Plattformen.
Wichtig: hohe False-Positive-Rate -> verification_service muss danach ran.
TODO: sherlock als Subprozess ODER die site-Liste selbst abklappern."""
from app.connectors.base import BaseConnector
from app.core.registry import register_connector
from app.schemas.connector import ConnectorCapability, RunContext
from app.schemas.enums import SelectorType, FindingType
from app.schemas.selector import SelectorOut
from app.schemas.finding import RawFinding


class SherlockConnector(BaseConnector):
    capability = ConnectorCapability(
        name="sherlock",
        version="0.1.0",
        accepts={SelectorType.USERNAME},
        produces={FindingType.ACCOUNT},
        reliability=0.4,               # bewusst niedrig -> Verifikation zwingend
    )

    async def fetch(self, selector: SelectorOut, ctx: RunContext) -> list[RawFinding]:
        # TODO: pro Treffer RawFinding(type=ACCOUNT, url=..., verified bleibt False)
        #       produced_selectors ggf. (URL, profil_url)
        raise NotImplementedError("Sherlock-Fetch implementieren")


register_connector(SherlockConnector())
