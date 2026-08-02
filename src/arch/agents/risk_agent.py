"""Phase REPORT. Formuliert Priorisierung und Remediation aus den BEREITS
berechneten Scores. Rechnet selbst NICHTS -> sonst nicht reproduzierbar.
Produziert RISK_NOTE (Text), keine Zahlen."""
from app.agents.base import BaseAgent
from app.core.registry import register_agent
from app.schemas.agent import AgentContext, Proposal
from app.schemas.enums import Phase


class RiskAgent(BaseAgent):
    name = "risk"
    phase = Phase.REPORT

    def build_prompt(self, ctx: AgentContext) -> str:
        # ctx.payload enthaelt fertige RiskItems inkl. chain_score.
        # Der Agent erklaert und priorisiert, er ueberschreibt keine Scores.
        raise NotImplementedError

    def parse(self, raw: dict) -> list[Proposal]:
        raise NotImplementedError


register_agent(RiskAgent())
