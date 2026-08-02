"""Eine aufgeloeste Identitaet: Cluster aus Findings."""
import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from app.models.base import Base, TimestampMixin


class Entity(Base, TimestampMixin):
    __tablename__ = "entities"
    id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subject_id: Mapped[uuid.UUID] = mapped_column(String, index=True)
    label: Mapped[str] = mapped_column(String(256))
    is_subject_self: Mapped[bool] = mapped_column(default=False)   # ist das die Zielperson?
