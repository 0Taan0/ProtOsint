"""Finding-Schemas. Ein Finding ist ein normalisiertes Connector-Ergebnis."""
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field
from app.schemas.enums import FindingType, SelectorType


class Provenance(BaseModel):
    """Herkunftsnachweis. MUSS an jedem Finding hängen, sonst nicht
    nachvollziehbar und nicht deduplizierbar."""
    connector_name: str
    connector_version: str
    fetched_at: datetime
    source_selector_id: UUID


class RawFinding(BaseModel):
    """Was ein Connector zurückgibt, bevor der Kern es persistiert."""
    type: FindingType
    label: str                            # menschenlesbar, z.B. "GitHub @taan"
    url: str | None = None
    attributes: dict = Field(default_factory=dict)   # frei, connector-spezifisch
    raw: dict = Field(default_factory=dict)          # Roh-Payload für Audit
    produced_selectors: list[tuple[SelectorType, str]] = Field(default_factory=list)


class FindingOut(BaseModel):
    id: UUID
    type: FindingType
    label: str
    url: str | None
    attributes: dict
    provenance: Provenance
    fingerprint: str
    verified: bool = False
    confidence: float = Field(default=0.0, ge=0, le=1)

    model_config = {"from_attributes": True}
