"""Phase VERIFY. Der wichtigste Agent: gehoert ein Account plausibel zur
Zielperson oder teilt er nur denselben String? Produziert ENTITY_LINK.
Zuerst ausbauen -- groesster Qualitaetssprung, sofort gegen eigenes Wissen pruefbar."""
from app.agents.base import BaseAgent
from app.core.registry import register_agent
from app.schemas.agent import AgentContext, Proposal
from app.schemas.enums import Phase, ProposalKind


class AttributionAgent(BaseAgent):
    name = "attribution"
    phase = Phase.VERIFY

    def build_prompt(self, ctx: AgentContext) -> str:
        # Input aus ctx.payload: Kandidaten-Finding + bereits gesicherte Merkmale
        # der Zielperson (Anzeigename, Zeitzone, Avatar-Hash, verlinkte Profile).
        # Frage ans LLM: gehoert das zusammen? Mit Begruendung und Evidenz-IDs.
        # TODO: Prompt schreiben. KEINE Klarnamen an die API -> pseudonymisieren.
        raise NotImplementedError

    def parse(self, raw: dict) -> list[Proposal]:
        # Erwartet JSON: {links: [{finding_id, target_entity, confidence, why}]}
        # Jeder Link -> Proposal(kind=ENTITY_LINK, evidence=[finding_id], ...)
        # TODO
        raise NotImplementedError

    def repair(self, raw: dict, err) -> list[Proposal]:
        # Beispiel-Naht: fehlende confidence -> 0.0 (faellt dann unter Schwelle)
        return []


register_agent(AttributionAgent())
