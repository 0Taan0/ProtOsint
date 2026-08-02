"""Selektor-Schemas. Ein Selektor ist ein Suchanker (Username, Mail, ...)."""
from uuid import UUID
from pydantic import BaseModel, Field
from app.schemas.enums import SelectorType


class SelectorIn(BaseModel):
    type: SelectorType
    value: str
    depth: int = 0                       # Pivot-Tiefe, Seeds = 0


class SelectorOut(SelectorIn):
    id: UUID
    origin_finding_id: UUID | None = None
    confidence: float = Field(default=1.0, ge=0, le=1)

    model_config = {"from_attributes": True}
