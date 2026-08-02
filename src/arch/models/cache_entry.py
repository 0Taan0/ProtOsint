"""Connector-Cache. Macht Iteration am Core deterministisch und billig."""
import uuid
from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID, JSONB
from app.models.base import Base, TimestampMixin


class CacheEntry(Base, TimestampMixin):
    __tablename__ = "cache_entries"
    id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    key: Mapped[str] = mapped_column(String(64), unique=True, index=True)   # sha256
    payload: Mapped[dict] = mapped_column(JSONB, default=dict)
    fetched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
