"""Die Policy-Naht. v1 sagt immer ja, v2 prueft Ownership."""
from typing import Protocol, runtime_checkable
from pydantic import BaseModel
from app.schemas.selector import SelectorOut


class SelectorDecision(BaseModel):
    allowed: bool
    may_pivot: bool
    reason: str


@runtime_checkable
class SelectorPolicy(Protocol):
    def evaluate(self, selector: SelectorOut, subject_id: str) -> SelectorDecision:
        ...
