"""STUB. RawFinding -> Finding. Setzt Fingerprint (Idempotenz) und Provenienz."""
import hashlib
from app.schemas.finding import RawFinding


def fingerprint(connector_name: str, rf: RawFinding) -> str:
    """Deterministisch -> dedupliziert und macht Laeufe vergleichbar."""
    basis = f"{connector_name}|{rf.type}|{rf.label}|{rf.url or ''}"
    return hashlib.sha256(basis.encode()).hexdigest()

# TODO: async def persist(run, selector, connector_name, version, rf) -> Finding
#       upsert per fingerprint, produced_selectors als neue Selector-Kandidaten
#       (depth+1) zurueckgeben.
