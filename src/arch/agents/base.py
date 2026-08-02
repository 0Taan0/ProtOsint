"""Agent-Basis. Kapselt LLM-Call, Structured-Output-Validierung und
Repair-statt-Retry. Konkrete Agenten liefern nur Prompt + Output-Schema."""
from abc import ABC, abstractmethod
from typing import ClassVar
from pydantic import BaseModel, ValidationError
from app.schemas.agent import AgentContext, AgentResult, Proposal
from app.schemas.enums import Phase
from app.core.logging import get_logger

log = get_logger("agent")


class BaseAgent(ABC):
    name: ClassVar[str]
    phase: ClassVar[Phase]

    async def run(self, ctx: AgentContext) -> AgentResult:
        prompt = self.build_prompt(ctx)
        raw = await self._call_llm(prompt)
        try:
            proposals = self.parse(raw)
        except ValidationError as e:
            log.warning("agent %s schema violation, repairing", self.name)
            proposals = self.repair(raw, e)         # deterministisch, kein Re-Prompt
        return AgentResult(proposals=proposals, tokens_used=raw.get("_tokens", 0))

    @abstractmethod
    def build_prompt(self, ctx: AgentContext) -> str:
        ...

    @abstractmethod
    def parse(self, raw: dict) -> list[Proposal]:
        ...

    def repair(self, raw: dict, err: ValidationError) -> list[Proposal]:
        """Default: nichts retten. Konkrete Agenten koennen Felder defaulten."""
        return []

    async def _call_llm(self, prompt: str) -> dict:
        # TODO: OpenAI-Call mit Structured Output. Findings pseudonymisiert
        #       schicken, Rueckmapping lokal. Bei fehlendem Key -> {} zurueck.
        raise NotImplementedError("LLM-Call in base._call_llm implementieren")
