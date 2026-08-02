"""Die Zielperson des Audits. In v1 == Betreiber."""
import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from app.models.base import Base, TimestampMixin


class Subject(Base, TimestampMixin):
    __tablename__ = "subjects"
    id: Mapped[uuid.UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    label: Mapped[str] = mapped_column(default="self")
    # v2: verified_owner, contact_email, ... -> Naht steht, Spalten spaeter
