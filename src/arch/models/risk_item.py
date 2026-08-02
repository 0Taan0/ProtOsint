import uuid
from sqlalchemy import ForeignKey, String, Float, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from app.models.base import Base, TimestampMixin


class RiskItem(Base, TimestampMixin):
    __tablename__ = "risk_items"
    id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    run_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("runs.id"))
    finding_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("findings.id"), nullable=True)
    title: Mapped[str] = mapped_column(String(256))
    discoverability: Mapped[float] = mapped_column(Float, default=0.0)
    identifiability: Mapped[float] = mapped_column(Float, default=0.0)
    sensitivity: Mapped[float] = mapped_column(Float, default=0.0)
    persistence: Mapped[float] = mapped_column(Float, default=0.0)
    score: Mapped[float] = mapped_column(Float, default=0.0)
    chain_score: Mapped[float] = mapped_column(Float, default=0.0)
    remediation: Mapped[str] = mapped_column(Text, default="")
    status: Mapped[str] = mapped_column(String(32), default="open")   # open|done|accepted
