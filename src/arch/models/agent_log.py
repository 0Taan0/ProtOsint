"""Vollstaendiges Protokoll jedes Agentenlaufs. Bei einem Werkzeug, das
ueber echte Personen urteilt, ist Nachvollziehbarkeit Pflicht."""
import uuid
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID, JSONB
from app.models.base import Base, TimestampMixin


class AgentLog(Base, TimestampMixin):
    __tablename__ = "agent_logs"
    id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    run_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("runs.id"))
    agent_name: Mapped[str] = mapped_column(String(64))
    prompt_version: Mapped[str] = mapped_column(String(32), default="v1")
    model: Mapped[str] = mapped_column(String(64), default="")
    input_hash: Mapped[str] = mapped_column(String(64), default="")
    raw_response: Mapped[dict] = mapped_column(JSONB, default=dict)
    accepted: Mapped[list] = mapped_column(JSONB, default=list)
    rejected: Mapped[list] = mapped_column(JSONB, default=list)
    tokens_used: Mapped[int] = mapped_column(Integer, default=0)
