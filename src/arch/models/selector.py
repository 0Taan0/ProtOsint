import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, String, Integer, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from app.models.base import Base, TimestampMixin
from app.schemas.enums import SelectorType


class Selector(Base, TimestampMixin):
    __tablename__ = "selectors"
    id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subject_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("subjects.id"))   # fuer RLS in v2
    type: Mapped[SelectorType] = mapped_column(String(32))
    value: Mapped[str] = mapped_column(String(512))
    depth: Mapped[int] = mapped_column(Integer, default=0)
    confidence: Mapped[float] = mapped_column(Float, default=1.0)
    origin_finding_id: Mapped[uuid.UUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("findings.id"), nullable=True
    )
    # v2-Naht, in v1 unbefuellt:
    verified_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    verification_method: Mapped[str | None] = mapped_column(String(64), nullable=True)
