"""Report-Schemas. Ausgabe von scoring_service + risk_agent."""
from pydantic import BaseModel, Field


class RiskItem(BaseModel):
    title: str
    discoverability: float = Field(ge=0, le=1)
    identifiability: float = Field(ge=0, le=1)
    sensitivity: float = Field(ge=0, le=1)
    persistence: float = Field(ge=0, le=1)
    score: float
    chain_score: float = 0.0              # kuerzester Pfad Pseudonym -> Klarname
    remediation: str = ""


class Report(BaseModel):
    run_id: str
    items: list[RiskItem] = Field(default_factory=list)
    summary: str = ""
