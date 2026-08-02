"""Kante zwischen zwei Entities. Traegt Evidenz und Confidence.
Ueber diese Tabelle laeuft spaeter die Pfadsuche (rekursive CTE)."""
import uuid
from sqlalchemy import ForeignKey, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID, JSONB
from app.models.base import Base, TimestampMixin
from app.schemas.enums import EdgeType


class Edge(Base, TimestampMixin):
    __tablename__ = "edges"
    id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    src_entity_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("entities.id"))
    dst_entity_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("entities.id"))
    type: Mapped[EdgeType] = mapped_column(String(32))
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
    evidence_ids: Mapped[list] = mapped_column(JSONB, default=list)   # Finding-IDs
