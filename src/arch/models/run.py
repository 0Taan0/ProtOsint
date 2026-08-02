import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import ForeignKey, String, Integer, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from app.models.base import Base, TimestampMixin
from app.schemas.enums import RunStatus, Phase


class Run(Base, TimestampMixin):
    __tablename__ = "runs"
    id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subject_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("subjects.id"))
    status: Mapped[RunStatus] = mapped_column(String(16), default=RunStatus.QUEUED)
    phase: Mapped[Phase] = mapped_column(String(16), default=Phase.SCOPING)
    max_depth: Mapped[int] = mapped_column(Integer, default=2)
    budget_cents: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=Decimal("0"))
    budget_spent: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=Decimal("0"))
    threshold: Mapped[float] = mapped_column(default=0.5)      # Confidence-Schwelle
    policy_name: Mapped[str] = mapped_column(String(64), default="local_owner")
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
