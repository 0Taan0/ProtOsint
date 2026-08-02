"""Phase ANALYZE. Klassifiziert Content/Metadaten in Sensitivitaetskategorien
und erkennt plattformuebergreifende Muster. Produziert CLASSIFICATION."""
from app.agents.base import BaseAgent
from app.core.registry import register_agent
from app.schemas.agent import AgentContext, Proposal
from app.schemas.enums import Phase


class AnalysisAgent(BaseAgent):
    name = "analysis"
    phase = Phase.ANALYZE

    def build_prompt(self, ctx: AgentContext) -> str:
        # WICHTIG: bekommt nie "alle Findings", sondern die von scoring/SQL
        # vorselektierten Top-N nach Sensitivitaets-Prefilter (ctx.evidence_ids).
        raise NotImplementedError

    def parse(self, raw: dict) -> list[Proposal]:
        raise NotImplementedError


register_agent(AnalysisAgent())
