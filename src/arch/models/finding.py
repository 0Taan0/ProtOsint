import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, String, Boolean, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID, JSONB
from app.models.base import Base, TimestampMixin
from app.schemas.enums import FindingType


class Finding(Base, TimestampMixin):
    __tablename__ = "findings"
    id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subject_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("subjects.id"))
    run_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("runs.id"))
    type: Mapped[FindingType] = mapped_column(String(32))
    label: Mapped[str] = mapped_column(String(512))
    url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    attributes: Mapped[dict] = mapped_column(JSONB, default=dict)
    raw: Mapped[dict] = mapped_column(JSONB, default=dict)
    # Provenienz flach mitgefuehrt:
    connector_name: Mapped[str] = mapped_column(String(64))
    connector_version: Mapped[str] = mapped_column(String(32))
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    source_selector_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("selectors.id"))
    # Deduplizierung + Verifikation:
    fingerprint: Mapped[str] = mapped_column(String(64), index=True)   # deterministisch
    verified: Mapped[bool] = mapped_column(Boolean, default=False)
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
