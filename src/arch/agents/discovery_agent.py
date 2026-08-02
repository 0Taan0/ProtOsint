"""Phase DISCOVER. Entscheidet, welche Selektorvarianten sich lohnen
(Schreibweisen, abgeleitete Usernames). Produziert NEW_SELECTOR-Proposals."""
from app.agents.base import BaseAgent
from app.core.registry import register_agent
from app.schemas.agent import AgentContext, Proposal
from app.schemas.enums import Phase


class DiscoveryAgent(BaseAgent):
    name = "discovery"
    phase = Phase.DISCOVER

    def build_prompt(self, ctx: AgentContext) -> str:
        # TODO: Seeds + bisherige Treffer -> plausible Selektorvarianten
        raise NotImplementedError

    def parse(self, raw: dict) -> list[Proposal]:
        raise NotImplementedError


register_agent(DiscoveryAgent())
