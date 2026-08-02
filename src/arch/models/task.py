"""Eine Connector-Ausfuehrung fuer einen Selektor. Macht Laeufe fortsetzbar."""
import uuid
from datetime import datetime
from sqlalchemy import ForeignKey, String, Integer, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from app.models.base import Base, TimestampMixin
from app.schemas.enums import TaskStatus


class Task(Base, TimestampMixin):
    __tablename__ = "tasks"
    id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    run_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("runs.id"))
    connector_name: Mapped[str] = mapped_column(String(64))
    connector_version: Mapped[str] = mapped_column(String(32))
    selector_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("selectors.id"))
    depth: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[TaskStatus] = mapped_column(String(16), default=TaskStatus.PENDING)
    attempts: Mapped[int] = mapped_column(Integer, default=0)
    last_error: Mapped[str | None] = mapped_column(Text, nullable=True)
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
